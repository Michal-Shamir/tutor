from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password',
                validators=[DataRequired(), Length(min=3, max=15)])
    confirm_password = PasswordField('Confirm Password',
                validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired()])
    password = PasswordField('Password',
                validators=[DataRequired()])
    remember = BooleanField('Remeber Me')
    submit = SubmitField('Login')