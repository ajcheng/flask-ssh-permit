# flask-ssh-permit
这是我用flask写的第一个和工作有点关系的项目,比较简陋，用于实现ssh权限申请添加的过程。

### 部署步骤

#### 1、安装虚拟环境sudo apt-get install virtualenv
#### 2、在目录里面执行virtualenv venv然后安装相应的依赖包 pip install -r requirements.txt
#### 3、修改数据库配置,在目录下执行python manage.py db init/upgrade/migrate
#### 4、安装gunicorn，pip install gunicorn然后使用gunicorn启动项目:gunicorn --workers=4 run:app -b 0.0.0.0:9000 -D -access-logfile access.log --error-logfile error.log
#### 5、前端可以nginx配置域名跳转

