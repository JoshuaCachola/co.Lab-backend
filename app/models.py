from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    Class for users model
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    hashed_pw = db.Column(db.String, nullable=False)
    avatar = db.Column(db.String)

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
