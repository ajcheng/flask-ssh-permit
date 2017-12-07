#encoding: utf-8

from flask import Flask,render_template,request,redirect,url_for,session
import config
from models import User,Authorith
from exts import db
from decorators import login_required
from sqlalchemy import or_
import paramiko,os,sys

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    alls = Authorith.query.order_by('-create_time').limit(5)
    return render_template('index.html',alls=alls)


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        if user and user.check_passwd(password):
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'用户名密码错误，请重新输入'

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        tel = request.form.get('tel')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #用户名验证
        user = User.query.filter(User.username == username).first()
        if user:
            return u'用户名已存在'
        else:
            #passwd判断
            if password1 != password2:
                return u'两次密码输入有误'
            else:
                user = User(tel=tel,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                print "注册成功"
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))

@app.route('/add/',methods=['GET','POST'])
@login_required
def add_authorith():

    if request.method == 'GET':
        return render_template('authorith.html')
    else:
        account = request.form.get('account')
        host = request.form.get('host')
        content = request.form.get('content')
        authorith = Authorith(account=account,host=host,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        authorith.author = user
        db.session.add(authorith)
        db.session.commit()
        #直接使用os.system调用shell脚本，注意脚本需要修改以及ssh_config需要配置
        #os.system('/home/aj/shell/1_add_key.sh %s %s duoduo' %(host,account))
        return redirect(url_for('user',user_id=user.username))


@app.route('/user/<user_id>/')
@login_required
def user(user_id):
    user_id = session.get('user_id')
    authoriths = Authorith.query.order_by('-create_time').filter(Authorith.author_id == user_id)
    return render_template('user.html', authoriths=authoriths)



@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}

if __name__ == '__main__':
    app.run()