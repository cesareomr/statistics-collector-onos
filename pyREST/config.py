# coding=utf-8
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'bbddtfg'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
