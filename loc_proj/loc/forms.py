from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	
	username= StringField('Username',validators=[DataRequired(),Length(min=2,max=10)])

	email= PasswordField('Email',validators=[DataRequired(), Email()])

	password= PasswordField('Password',validators=[DataRequired()])

	confirm_password= StringField('Confirm Password',validators=[DataRequired(), EqualTo('password')])

	submit=SubmitField('Sign Up')

	def validate_field(self,field):
		if True:
			raise ValidationError('Validation Message')


class LoginForm(FlaskForm):

	email= StringField('Email',validators=[DataRequired(), Email()])

	password= PasswordField('Password',validators=[DataRequired()])

	remember= BooleanField('Remember Me')

	submit=SubmitField('Log In')