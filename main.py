from app import create_app
from flask import render_template, session, redirect, url_for, make_response
from app.forms import LoginForm
from flask_login import login_required
import unittest

from app.firestore_services import get_users, get_todos

app = create_app()

@app.cli.command()
def test():
    """Ejecutar las pruebas del servidor"""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.route('/')
@login_required
def index():
    username = session.get('username')
    todos = get_todos(user_id=username)

    context = {
        'username': username,
        'todos': todos
    }

    return render_template('index.html', **context)
