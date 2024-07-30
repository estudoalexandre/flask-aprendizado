from flask_marshmallow import Marshmallow
from ..models import user_model
from api import ma
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ('id', 'username','idade', 'email', 'password_hash')

    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)


