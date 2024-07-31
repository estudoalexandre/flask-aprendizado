from api import ma
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

from api.models.posts_model import Post


class PostSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Post
        load_instance = True
        include_fk = True
        fields = ('id', 'title', 'content', 'user_id')

    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    content = fields.String(required=True)
    user_id = fields.Integer(load_only=True)
