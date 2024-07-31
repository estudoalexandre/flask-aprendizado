from ..models.posts_model import Post
from api import db

def get_all_posts():
    return Post.query.all()

def get_post_by_id(post_id):
    return Post.query.filter_by(id=post_id).first()

def create_post(post_data):
    new_post = Post(
        title=post_data['title'],
        content=post_data['content'],
        user_id=post_data['user_id']
    )
    db.session.add(new_post)
    db.session.commit()
    return new_post

def update_post(post_id, post_data):
    post = get_post_by_id(post_id)
    if post:
        post.title = post_data.get('title', post.title)
        post.content = post_data.get('content', post.content)
        post.user_id = post_data.get('user_id', post.user_id)
        db.session.commit()
        return post
    return None

def delete_post(post_id):
    post = get_post_by_id(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return post
    return None
