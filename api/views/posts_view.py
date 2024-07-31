from flask_restful import Resource
from flask import request, make_response, jsonify
from api import api
from api.services import posts_service
from ..schemas import posts_schemas

class PostList(Resource):
    def get(self):
        posts = posts_service.get_all_posts()
        ps = posts_schemas.PostSchema(many=True)
        result = ps.dump(posts)
        return make_response(jsonify(result), 200)

    def post(self):
        create_post = posts_schemas.PostSchema()
        validate = create_post.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            post_data = {
                'title': request.json['title'],
                'content': request.json['content'],
                'user_id': request.json['user_id']
            }
            new_post = posts_service.create_post(post_data)
            result = create_post.dump(new_post)
            return make_response(jsonify(result), 201)

class PostDetail(Resource):
    def get(self, id):
        post = posts_service.get_post_by_id(id)
        if post is None:
            return make_response(jsonify({'error': 'Post not found'}), 404)
        ps = posts_schemas.PostSchema()
        result = ps.dump(post)
        return make_response(jsonify(result), 200)

    def put(self, id):
        update_post = posts_schemas.PostSchema()
        validate = update_post.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            post_data = {
                'title': request.json.get('title'),
                'content': request.json.get('content'),
                'user_id': request.json.get('user_id')
            }
            updated_post = posts_service.update_post(id, post_data)
            if updated_post:
                result = update_post.dump(updated_post)
                return make_response(jsonify(result), 200)
            return make_response(jsonify({'error': 'Post not found'}), 404)

    def delete(self, id):
        deleted_post = posts_service.delete_post(id)
        if deleted_post:
            ps = posts_schemas.PostSchema()
            result = ps.dump(deleted_post)
            return make_response(jsonify(result), 200)
        return make_response(jsonify({'error': 'Post not found'}), 404)

api.add_resource(PostList, '/posts')
api.add_resource(PostDetail, '/posts/<int:id>')
