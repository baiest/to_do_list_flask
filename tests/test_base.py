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
        self.assertRedirects(response, url_for(login_manager.login_view) + '?next=%2F')

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)
    
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        self.assertTrue(response.status_code, 405)

    def test_login_user(self):
        user_fake = {
            'username': 'bernardo',
            'password': 'password'
        }

        response = self.client.post(url_for('auth.login'), data=user_fake)
        self.assertRedirects(response, url_for('index'))
