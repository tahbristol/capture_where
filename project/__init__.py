from flask import Flask 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import project.env as ENV

app = Flask(__name__)
ma = Marshmallow(app)
CORS(app)
app.config['SECRET_KEY'] = 'EKJwxeyH\x04W7@6P]1\x11`ku)`g8\u061cn|S/OC3%2A1s('
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from project import routes