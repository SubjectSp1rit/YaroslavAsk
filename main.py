from flask import Flask, render_template, redirect
from data import LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


# главная страница
@app.route("/")
def index():
    return render_template('index.html')


# вход в аккаунт
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # ПОСЛЕ ТОГО КАК USER НАЖАЛ ВОЙТИ ЗАПРАШИВАЕМ У БД ДАННЫЕ И СРАВНИВАЕМ ИХ
    # form.login.data СОДЕРЖИТ ЛОГИН USER'А
    # form.password.data содержит пароль
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            print('ВХОД ВЫПОЛНЕН УСПЕШНО!')
            # если все ок, вход выполнен - переадресовываем на главную страницу
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


# выход из аккаунта
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    app.run()
