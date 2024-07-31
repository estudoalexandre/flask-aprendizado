
from api import db
from ..models.comments_model import Comments

def get_all_posts():
    return Comments.query.all()

def get_comment_by_id(comment_id):
    return Comments.query.filter_by(id=comment_id).first()

def create_post(post_data):
    new_comment = Comments(
        content=post_data['content'],
        post_id=post_data['post_id'],
        user_id=post_data['user_id']
    )
    db.session.add(new_comment)
    db.session.commit()
    return new_comment

def update_post(comment_id, comment_data):
    comment = get_comment_by_id(comment_id)
    if comment:
        comment.content = comment_data.get('content', comment.content)
        comment.title = comment_data.get('title', comment.post_id)
        comment.user_id = comment_data.get('user_id', comment.user_id)
        db.session.commit()
        return comment
    return None

def delete_post(comment_id):
    comment = get_comment_by_id(comment_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return comment
    return None
