from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import Required, length


class LoginForm(FlaskForm):
    '''
    Accepts a nickname and a room
    '''
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    room = StringField('Room', validators=[Required()])
    submit = SubmitField('Enter Chatroom')


class RegisterForm(FlaskForm):
    '''
    Accepts username, password, first_name, and last_name to create a new user account
    '''
    username = StringField('Username', validators=[Required(), length(max=16)])
    password = PasswordField('Password', validators=[
                             Required(), length(max=60)])
    password_conf = PasswordField('Confirm Password', validators=[
                                  Required(), length(max=50)])
    first_name = StringField('First Name', validators=[
                             Required(), length(max=50)])
    last_name = StringField('Last Name', validators=[
                            Required(), length(max=50)])
    submit = SubmitField('Register')
