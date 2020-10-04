from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField


app=Flask(__name__)
app.secret_key='hello'

class LoginForm(FlaskForm):
    username = StringField('用户名:',description='用户名')
    password = PasswordField('密码:',description='密码')
    password2 = PasswordField('确认密码:',description='确认密码')
    submit = SubmitField('提交')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm() 
    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    