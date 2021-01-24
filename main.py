from app import create_app
from flask import render_template, session, redirect, url_for, make_response
from app.forms import LoginForm
import unittest

app = create_app()

@app.cli.command()
def test():
    """Ejecutar las pruebas del servidor"""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.route('/')
def index():
    username = session.get('username')
    if not session.get('username'):
        response = make_response(redirect('/login'))
        return response

    return render_template('index.html', username=username)
