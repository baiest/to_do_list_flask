from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from .config import Config
from .auth import auth

login = LoginManager()
login.login_view = 'auth.login'

@login.user_loader
def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    login.init_app(app)

    app.register_blueprint(auth)

    return app