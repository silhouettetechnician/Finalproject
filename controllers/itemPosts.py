from flask import Blueprint, request, jsonify, g
from lib.login_required import login_required
from models.itemPost import ItemPost, ItemPostSchema, Comment, CommentSchema
from models.designer import Designer

itemPost_schema = ItemPostSchema()
comment_schema = CommentSchema()

api = Blueprint('posts', __name__)


@api.route('/posts', methods=['GET'])
def index():

    posts = ItemPost.query.all()

    return itemPost_schema.jsonify(posts, many=True), 200


@api.route('/posts/<int:post_id>', methods=['GET'])
def show(post_id):

    post = ItemPost.query.get(post_id)

    return itemPost_schema.jsonify(post), 200

@api.route('/posts', methods=['POST'])
@login_required
def create():
    data = request.get_json()
    post, errors = itemPost_schema.load(request.get_json())

    if errors:
        return jsonify(errors, 422)

    designer = Designer.query.get(data['designer_id'])

    post.creator = g.current_user
    post.designers.append(designer)
    post.save()
    return itemPost_schema.jsonify(post)

@api.route('/posts/<int:posts_id>', methods=['PUT'])
@login_required
def update(post_id):
    post = ItemPost.query.get(post_id)
    post, errors = itemPost_schema.load(request.get_json(), instance=post, partial=True)

    if errors:
        return jsonify(errors, 422)

    if post.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401

    post.save()
    return itemPost_schema.jsonify(post)

@api.route('/posts/<int:post_id>', methods=["DELETE"])
@login_required
def delete(post_id):
    post = ItemPost.query.get(post_id)
    if post.creator != g.current_user:
        return jsonify({'message': 'Unauthorized'}), 401
    post.remove()
    return '', 204

@api.route('/posts/<int:post_id>/comments', methods=['POST'])
@login_required
def comment_create(post_id):
    data = request.get_json()
    post = ItemPost.query.get(post_id)
    comment, errors = comment_schema.load(data)
    if errors:
        return jsonify(errors), 422
    comment.post = post
    comment.save()
    return comment_schema.jsonify(comment)

@api.route('/posts/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
@login_required
def comment_delete(**kwargs):
    comment = Comment.query.get(kwargs['comment_id'])
    comment.remove()
    return '', 204


@api.route('/posts/<int:post_id>/like', methods=['POST'])
@login_required
def like(post_id):
    post = ItemPost.query.get(post_id)
    user = g.current_user
    post.liked_by.append(user)
    post.save()
    return itemPost_schema.jsonify(post), 201
