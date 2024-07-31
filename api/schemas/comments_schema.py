from api import ma
from ..models import comments_model
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from api import ma


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = comments_model.Comments
        include_fk = True
        load_instance = True

        id = fields.Integer(dump_only=True)
        content = fields.Str(required=True)
        post_id = fields.Integer(required=True)
        user_id = fields.Integer(required=True)


