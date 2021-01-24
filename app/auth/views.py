from . import auth
from flask import render_template, redirect, url_for, session
from app.forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Pagina para loguear al usuario con sus credenciales"""
    username = session.get('username')
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        return redirect(url_for('index'))

    return render_template('login.html', login_form=login_form) 
