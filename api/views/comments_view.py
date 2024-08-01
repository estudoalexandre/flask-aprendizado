from flask_restful import Resource
from flask import request, make_response, jsonify
from api import api
from api.services import comments_service
from ..schemas import comments_schema

class CommentsList(Resource):
    def get(self):
        comments = comments_service.get_all_posts()
        ps = comments_schema.CommentSchema(many=True)
        result = ps.dump(comments)
        return make_response(jsonify(result), 200)

    def post(self):
        create_comments = comments_schema.CommentSchema()
        validate = create_comments.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            post_data = {
                'content': request.json['content'],
                'post_id': request.json['post_id'],
                'user_id': request.json['user_id']
            }
            new_comment = comments_service.create_post(post_data)
            result = create_comments.dump(new_comment)
            return make_response(jsonify(result), 201)

class CommentsDetail(Resource):
    def get(self, id):
        post = comments_service.get_post_by_id(id)
        if post is None:
            return make_response(jsonify({'error': 'Post not found'}), 404)
        ps = comments_schema.CommentSchema()
        result = ps.dump(post)
        return make_response(jsonify(result), 200)

    def put(self, id):
        update_post = comments_schema.CommentSchema()
        validate = update_post.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            post_data = {
                'content': request.json.get('content'),
                'post_id': request.json.get('post_id'),
                'user_id': request.json.get('user_id')
            }
            updated_post = comments_service.update_post(id, post_data)
            if updated_post:
                result = update_post.dump(updated_post)
                return make_response(jsonify(result), 200)
            return make_response(jsonify({'error': 'Comment not found'}), 404)

    def delete(self, id):
        deleted_post = comments_service.delete_post(id)
        if deleted_post:
            ps = comments_schema.CommentSchema()
            result = ps.dump(deleted_post)
            return make_response(jsonify(result), 200)
        return make_response(jsonify({'error': 'Post not found'}), 404)


api.add_resource(CommentsList, '/comments')
api.add_resource(CommentsDetail, '/comments/<int:id>')
