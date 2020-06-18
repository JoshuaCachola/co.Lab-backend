from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config
from .routes import api, beats
from .models import db


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api.bp)
app.register_blueprint(beats.bp)
cors = CORS(app, resources={r'/*': {'origin': '*'}})
db.init_app(app)
Migrate(app, db)
