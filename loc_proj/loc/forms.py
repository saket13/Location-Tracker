from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from flask_login  import current_user 
from wtforms import StringField,SubmitField,PasswordField,BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from loc.models import User

class RegistrationForm(FlaskForm):
	
	username= StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])

	email= PasswordField('Email',validators=[DataRequired(), Email()])

	password= PasswordField('Password',validators=[DataRequired()])

	confirm_password= StringField('Confirm Password',validators=[DataRequired(), EqualTo('password')])

	submit=SubmitField('Sign Up')

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken .Please choose another username')

	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken .Please choose another email')


class LoginForm(FlaskForm):

	email= StringField('Email',validators=[DataRequired(), Email()])

	password= PasswordField('Password',validators=[DataRequired()])

	remember= BooleanField('Remember Me')

	submit=SubmitField('Log In')

class UpdateAccountForm(FlaskForm):
	
	username= StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])

	email= PasswordField('Email',validators=[DataRequired(), Email()])

	picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])

	submit=SubmitField('Update')

	def validate_username(self,username):
		if username.data != current_user.username:
			user=User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken .Please choose another username')

	def validate_email(self,email):
		if email.data != current_user.email :
			user=User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken .Please choose another email')

class LocationForm(FlaskForm):

	message = TextAreaField('Message',validators=[DataRequired()])

	submit = SubmitField('Share your location')     











