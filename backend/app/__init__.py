"""import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messaging_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('config.py')

#app = Flask(__name__)
#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'messaging_app.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes.auth import auth_bp
from app.routes.messages import messages_bp
from app.routes.main import main_bp
from app.utils.decorators import validate_json 

app.register_blueprint(auth_bp)
app.register_blueprint(messages_bp)
app.register_blueprint(main_bp)"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_file='config.py'):
    app = Flask(__name__, static_folder="../frontend/public", static_url_path="")
    print(app.template_folder)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messaging_app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.auth import auth_bp
    from app.routes.messages import messages_bp
    from app.routes.main import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(messages_bp)
    app.register_blueprint(main_bp)

    return app