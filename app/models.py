from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """
    Class for users model
        - UserMixin allows the usage of is_authenticated in session.py
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    hashed_pw = db.Column(db.String, nullable=False)
    avatar = db.Column(db.String)

    @property
    def password(self):
        return self.hashed_pw

    @password.setter
    def password(self, pw):
        self.hashed_pw = generate_password_hash(pw)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'hashed_pw': self.hashed_pw
        }


class Beat(db.Model):
    """
    Class for beats model
    """
    __tablename__ = 'beats'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    cover_art = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'cover_art': self.cover_art
        }
