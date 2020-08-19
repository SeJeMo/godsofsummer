from app import db
from datetime import datetime
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(120), default="PLAYER")
    about_me = db.Column(db.String(256))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    season_goals = db.Column(db.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, username):
        s = Settings.query.filter_by(username=username).first()
        if s is not None:
            return s.avatar.data
        return "/static/images/generic-avatar.jpg"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), index=True)

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)

    def __repr__(self):
        return '<Score {}>'.format(self.score)

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    avatar = db.Column(db.String(256), default="")
    username=db.Column(db.String, db.ForeignKey('user.username'), index=True, unique=True)