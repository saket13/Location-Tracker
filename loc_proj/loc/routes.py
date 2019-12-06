import os
import secrets
from flask import render_template,url_for,flash,redirect,request
from loc import app, db, bcrypt, gm
from loc.models import User,Post
from loc.forms import RegistrationForm, LoginForm, UpdateAccountForm , LocationForm
from flask_login import login_user,current_user,logout_user, login_required 

from flask_googlemaps import Map

@app.route("/")
@app.route("/home")

def home():
    locations = Post.query.all()
    return render_template('home.html',posts=locations) 

@app.route("/about")
def about():
    return render_template('about.html',title='about') 

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page= request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccesfull.Please check email and password','danger')

    return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn)
    form_picture.save(picture_path)

    return picture_fn

@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file=picture_file
        current_user.username=form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!','success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
    return render_template('account.html',title='Account',image_file=image_file,form=form)
 

from urllib.request import urlopen
from requests import get
def get_global_ip():
    my_ip = urlopen('http://ip.42.pl/raw').read()
    return my_ip.decode("utf-8")


def get_country(ip_address):
    try:
        response = requests.get("http://ip-api.com/json/{}".format(IPAddr))
        js = response.json()
        country = js['city']
        return country
    except Exception as e:
        return "Unknown"


@app.route("/location/new", methods=['GET','POST'])
@login_required
def new_location():
    form = LocationForm()
    IPAddr = '14.139.240.247'
    region = get_country(IPAddr)
    if form.validate_on_submit():
        post = Post(message=form.message.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your location has been shared','success')
        return redirect(url_for('home'))
    return render_template('create_loc.html',title='New Location',form=form)

# ADDED
@app.route('/map', methods=["GET"])
def my_map():
    mymap = Map(

                identifier="view-side",

                varname="mymap",

                style="height:720px;width:1100px;margin:0;", # hardcoded!

                lat=37.4419, # hardcoded!

                lng=-122.1419, # hardcoded!

                zoom=15,

                markers=[(37.4419, -122.1419)] # hardcoded!

            )

    return render_template('maps.html', mymap=mymap)






