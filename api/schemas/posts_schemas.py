from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields


class PostSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    content = fields.String(required=True)
    user_id = fields.Integer(dump_only=True)
