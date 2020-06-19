from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from .config import Config
from .routes import api, beats, auth
from .models import db, User


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api.bp)
app.register_blueprint(beats.bp)
app.register_blueprint(auth.bp)
cors = CORS(app, resources={r'/*': {'origin': '*'}})
db.init_app(app)
Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
