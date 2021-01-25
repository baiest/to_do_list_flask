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

def get_todos(user_id):
    todos = db.collection('users')\
        .document(user_id)\
        .collection('todos').get()
    
    return todos

def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})