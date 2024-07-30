from ..entidades import user
from flask_restful import Resource
from .. import api, db
from ..schemas import user_schema
from flask import request, make_response, jsonify
from ..services import user_service


class UserList(Resource):
    def get(self):
        users = user_service.get_all_users()
        us = user_schema.UserSchema(many=True)
        result = us.dump(users)
        return make_response(jsonify(result), 200)

    def post(self):
        create_user = user_schema.UserSchema()
        validate = create_user.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            username = request.json['username']
            idade = request.json['idade']
            email = request.json['email']
            password_hash = request.json['password_hash']

            new_user = user.User(username=username,
                                 idade=idade,
                                 email=email,
                                 password_hash=password_hash)

            results = user_service.create_user(new_user)
            return make_response(jsonify(results), 201)


class DetailUser(Resource):
    def get(self, id):
        user = user_service.get_user_by_id(id)
        if user is None:
            return make_response(jsonify({'error': 'User not found'}), 404)

        us = user_schema.UserSchema()
        result = us.dump(user)
        return make_response(jsonify(result), 200)

    def delete(self):
        pass


api.add_resource(UserList, '/users')
api.add_resource(DetailUser, '/users/<int:id>')
