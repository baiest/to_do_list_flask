from app import create_app
from flask import render_template, session, redirect, url_for, flash
from app.forms import TodoForm, DeleteTodoForm, UpdateTodoForm
from flask_login import login_required, current_user
import unittest

from app.firestore_services import get_todos, put_todo, delete_todo, update_todo

app = create_app()

@app.cli.command()
def test():
    """Ejecutar las pruebas del servidor"""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    username = current_user.id
    todos = get_todos(user_id=username)
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()
    context = {
        'username': username,
        'todos': todos,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form
    }

    if todo_form.validate_on_submit():
        put_todo(username, todo_form.description.data)

        flash('Tu tarea fue creada')

        return redirect(url_for('index'))

    return render_template('index.html', **context)

@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('index'))

@app.route('/todos/delete/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id, todo_id, done)

    return redirect(url_for('index'))

