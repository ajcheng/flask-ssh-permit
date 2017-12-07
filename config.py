#encoding: utf-8

import os

DEBUG = True
SECRET_KEY = os.urandom(24)

#通过如下命令创建远程可登录的mysql用户
#GRANT ALL PRIVILEGES ON ssh.* TO 'flask'@'%' identified by 'password';
HOSTNAME = '192.168.1.10'
PORT = '3306'
DATABASE = 'ssh'
USERNAME = 'flask'
PASSWORD = 'Flask#@KFEC!!@#'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

