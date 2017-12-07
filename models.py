#encoding: utf-8

from  exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    tel = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)

    def __init__(self,*args,**kwargs):
        tel = kwargs.get('tel')
        username = kwargs.get('username')
        password = kwargs.get('password')

        self.tel = tel
        self.username = username
        self.password = generate_password_hash(password)

    def check_passwd(self,raw_passwd):
        result = check_password_hash(self.password,raw_passwd)
        return result

class Authorith(db.Model):
    __tablename__ = 'authorith'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    account = db.Column(db.String(100),nullable=False)
    host = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref=db.backref('authorith'))
