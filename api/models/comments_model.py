from api import db
from ..entidades.user import User
from ..entidades.posts import Posts

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    post = db.relationship('Post', backref=db.backref('comments', lazy=True))
    user = db.relationship('User', backref=db.backref('comments', lazy=True))