from flask import Blueprint, jsonify, request, g
from models.user import User, UserSchema, CommentUser, CommentUserSchema
from lib.assistance import is_unique
from lib.login_required import login_required

api = Blueprint('auth', __name__)
user_schema = UserSchema()
comment_schema = CommentUserSchema()

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user, errors = user_schema.load(data)

    if not is_unique(model=User, key='username', value=data['username']):
        errors['username'] = errors.get('username', []) + ['Username already in use']

    if not is_unique(model=User, key='email', value=data['email']):
        errors['email'] = errors.get('email', []) + ['Email address already in use']

    if errors:
        return jsonify(errors), 422

    user.save()

    return jsonify({'message': 'Registration Succesful'}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not user.validate_password(data.get('password', '')):
        return jsonify({'message': 'Unauthorized'}), 401

    return jsonify({
    'message': 'Welcome back {}!'.format(user.username),
    'token': user.generate_token()
    })

@api.route('/profile', methods=['GET'])
@login_required
def show():
    print(g.current_user)
    return user_schema.jsonify(g.current_user), 200

@api.route('/users/<int:users_id>', methods=['GET'])
def show_user(users_id):

    users = User.query.get(users_id)
    return user_schema.jsonify(users), 200


@api.route('/users', methods=['GET'])
def show_users():

    users = User.query.all()

    return user_schema.jsonify(users, many=True), 200



# ***********************COMMENTS ********************************

@api.route('/users/<int:users_id>/comments', methods=['POST'])
@login_required
def comment_create_comment(users_id):
    data = request.get_json()
    user = User.query.get(users_id)
    comment, errors = comment_schema.load(data)
    if errors:
        return jsonify(errors), 422
    comment.user = user
    comment.creator = g.current_user
    comment.save()
    return comment_schema.jsonify(comment)

@api.route('/users/<int:users_id>/comments/<int:comment_id>', methods=['DELETE'])
@login_required
def comment_delete(**kwargs):
    comment = CommentUser.query.get(kwargs['comment_id'])
    comment.remove()
    return '', 204
