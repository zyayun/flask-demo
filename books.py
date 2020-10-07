from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,IntegerField

app = Flask(__name__)

#TODO 数据库配置
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@root:127.0.0.1/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

'''
图书馆小项目测试
项目需求:
1、数据库连接
2、数据库需求
    a、作者模型 
    b、书籍模型
3、form表单展示
    a、作者表单
    b、书籍表单
4、数据模型CRUD
'''

# 添加作者和书模型
class Author(db.Model):
    __tablename__ = 'authors'

   id = db.Column(db.)



    


@app.route('/')
def index():


    return "hello"

if __name__ == '__main__':
    app.run(debug=True)


    


