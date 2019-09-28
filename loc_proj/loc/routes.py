from flask import render_template,url_for,flash,redirect
from loc import app, db, bcrypt
from loc.models import User,Post
from loc.forms import RegistrationForm, LoginForm


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
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        user= User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created and you are now able to login !','success')
        return redirect(url_for('login'))
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