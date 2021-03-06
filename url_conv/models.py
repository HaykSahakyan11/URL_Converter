from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    suggestions = db.relationship('Suggestions', backref='author', lazy=True)
    urls = db.relationship('URL', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Suggestions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    reviewed_by_adm = db.Column(db.BOOLEAN, nullable=False, default=False)

    def __repr__(self):
        return f"URL('<<{self.url}>> - ', '{self.content}')"


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False)
    name = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"URL('<<{self.url}>> - ', '{self.name}')"