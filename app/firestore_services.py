import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

PROJECT_ID = 'to-do-list-flask-d3dcc'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {
    'projectId': PROJECT_ID
})

db = firestore.client()

def get_users():
    users = db.collection('users').get()
    return users

def get_user(user_id):
    return db.collection('users').document(user_id).get()

def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})

def get_todos(user_id):
    todos = db.collection('users')\
        .document(user_id)\
        .collection('todos').get()
    
    return todos

def put_todo(user_id, description):
    to_do_collection_ref = db.collection('users').document(user_id).collection('todos')
    to_do_collection_ref.add({'description': description, 'done': False})

def delete_todo(user_id, todo_id):
    #todo_ref = deb.collection('users').document(user_id).collection('todos').document(todo_id)
    todo_ref = db.document(f'users/{user_id}/todos/{todo_id}')
    todo_ref.delete()