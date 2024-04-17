from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, SelectField, IntegerField, FileField
from wtforms.validators import DataRequired, ValidationError


# Формы, которые используются html-файлами для сбора информации
class LoginForm(FlaskForm):
    login = TextAreaField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
