from app import create_app
from flask import render_template, session, redirect, url_for
from forms import LoginForm
import unittest

app = create_app()

@app.cli.command()
def test():
    """Ejecutar las pruebas del servidor"""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """"""
    username = session.get('username')
    login_form = LoginForm()
    context = {
        'username': username,
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        return redirect(url_for('index', **context))

    return render_template('login', **context) 