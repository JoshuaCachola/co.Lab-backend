from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime
import jwt
import os


db = SQLAlchemy()


class User(db.Model, UserMixin):
    """
    Class for users model
        - UserMixin allows the usage of is_authenticated in session.py
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_pw = db.Column(db.String, nullable=False)
    avatar = db.Column(db.String)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.hashed_pw = generate_password_hash(password, 'sha256')
        # self.hashed_pw = password
        self.registered_on = datetime.datetime.now()

    def check_password(self, password):
        return check_password_hash(self.hashed_pw, password)

    def encode_auth_token(self, user_id):
        """
        Generates JWT Token
        """
        try:
            payload = {'exp': datetime.datetime.utcnow() + datetime.timedelta(
                days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload,
                              os.environ.get('SECRET_KEY'),
                              algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token,
                                 app.config.get('SECRET_KEY'),
                                 algorithm='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'hashed_pw': self.hashed_pw
        }


# class Beat(db.Model):
#     """
#     Class for beats model
#     """
#     __tablename__ = 'beats'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     url = db.Column(db.String, nullable=False)
#     cover_art = db.Column(db.String)

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'url': self.url,
#             'cover_art': self.cover_art
#         }
