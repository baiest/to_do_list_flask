from . import auth
from flask import render_template, redirect, url_for, session, flash
from app.forms import LoginForm
from flask_login import login_user, login_required, logout_user, current_user

from app.firestore_services import get_user, user_put
from app.models import UserData, UserModel

from werkzeug.security import  generate_password_hash, check_password_hash

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Pagina para loguear al usuario con sus credenciales"""
    username = session.get('username')
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user(username)
        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']

            if check_password_hash(password_from_db, password):
                user_data = UserData(username, password)
                user = UserModel(user_data)
                login_user(user)
                flash('Bienvenido de nuevo')
                return redirect(url_for('index'))
            else:
                flash('La informacion no coincide')
        else:
            flash('El usuario no existe')
    return render_template('login.html', login_form=login_form) 

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))

@auth.route('signup', methods=['GET', 'POST'])
def signup():
    
    signup_form = LoginForm()
    context = {
        'signup_form':signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)
            login_user(user)
            flash('Bienvenido')

            return redirect(url_for('index'))
        else:
            flash('Este usuario ya existe')
    return render_template('signup_form.html', **context)