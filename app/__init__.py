from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'blog.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'denno'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Initialise our db
    db.init_app(app)

    # import our blueprints
    from .auth import auth
    from .main import main
    # registering blueprints
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(main, url_prefix='/')

    # import our db object classes
    from .models import User

    create_database(app)

    return app


# create our db
def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print('Database has been created')
