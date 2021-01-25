from flask_testing import TestCase
from flask import current_app, url_for
from main import app
from app import login_manager

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('auth.login') + '?next=%2F')

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)
    
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        self.assertTrue(response.status_code, 405)

  
    def test_login_and_logout_user(self):
        user_fake = {
            'username': 'Juan',
            'password': 'pass'
        }

        login = self.client.post(url_for('auth.login'), data=user_fake)
        self.assertRedirects(login, url_for('index'))
        
        logout = self.client.get(url_for('auth.logout'))
        self.assertRedirects(logout, url_for('auth.login'))

    def test_signup_user(self):
        new_user = {
            'username': 'nuevo',
            'password': '1234'
        }

        response = self.client.post(url_for('auth.signup', data=new_user))
        self.assert200(response)