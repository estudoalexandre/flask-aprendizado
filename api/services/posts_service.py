from ..models import user_model
from .. import db


def create_user(user):
    new_user = user_model.User(username=user.username,
                               idade=user.idade,
                               email=user.email,
                               password_hash=user.password_hash)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_all_users():
    all_users = user_model.User.query.all()
    return all_users


def get_user_by_id(user_id):
    user = user_model.User.query.filter_by(id=user_id).first()
    return user


def get_user_by_email(email):
    user_email = user_model.User.query.filter_by(email=email).first()
    return user_email


def update_user(user_antigo, novo_user):
    user_antigo.username = novo_user.username
    user_antigo.idade = novo_user.idade
    user_antigo.email = novo_user.email
    user_antigo.password_hash = novo_user.password_hash
    db.session.commit()


def delete_user(user_id):
    db.session.delete(user_id)
    db.session.commit()
