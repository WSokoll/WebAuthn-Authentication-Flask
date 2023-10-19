from datetime import datetime

from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
security = Security()


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=False,
        static_folder='static',
        static_url_path='/static'
    )

    app.config.from_pyfile('config.default.py')
    app.config.from_pyfile('../local/config.local.py')

    app.config["SECURITY_DATETIME_FACTORY"] = datetime.now
    app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}"
                                             f"@{app.config['DB_HOST']}/{app.config['DB_NAME']}")

    db.init_app(app)

    from app.models import User, Role, WebAuthn
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    user_datastore.webauthn_model = WebAuthn

    security.init_app(app, user_datastore)

    from app.views.example import bp as bp_example
    app.register_blueprint(bp_example)

    return app
