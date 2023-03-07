from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flaskloanapp.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskloanapp.employers.routes import employers
    from flaskloanapp.customers.routes import customers
    from flaskloanapp.main.routes import main
    from flaskloanapp.errors.handlers import errors
    app.register_blueprint(employers)
    app.register_blueprint(customers)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app