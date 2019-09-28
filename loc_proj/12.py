from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)


import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from models import User,Post


locations=[
        {
            'user':'Saket',
            'loc':'IIITM Campus, Gwalior',
            'date':'20 sep,19',
            'message': 'Sharing only purposefully'
         },
        {
            'user':'Ankur',
            'loc':'Kullo,Shimla',
            'date':'20 sep,2019',
            'message': 'Needs help'
         }
        ]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html',posts=locations) 

@app.route("/about")
def about():
    return render_template('about.html',title='about') 

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and  form.password.data=='password':
            flash('You have been logged in !','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesfull.Please check username and password','danger')

    return render_template('login.html',title='Login',form=form)



if __name__=='__main__':
    app.run(debug=True)

    
    
        
