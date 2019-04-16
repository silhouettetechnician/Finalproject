from datetime import datetime, timedelta
from sqlalchemy.ext.hybrid import hybrid_property
from app import db, ma, bcrypt
import jwt
from config.environment import secret
from marshmallow import validates_schema, ValidationError, validate, fields
from .base import BaseModel, BaseSchema
# pylint: disable=E1101


class User(db.Model, BaseModel):

    __tablename__ = 'users'

    name = db.Column(db.String(40))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    image = db.Column(db.String(500))
    password_hash = db.Column(db.String(130))
    discounts = db.Column(db.String(70))
    brand_likes = db.Column(db.String(70), nullable=True)

    # brand_discounts = db.relationship('ItemPost', secondary='post')


    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, plaintext):
        self.password_hash = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def validate_password(self, plaintext):
        return bcrypt.check_password_hash(self.password_hash, plaintext)

    def generate_token(self):
        payload = {

        'exp':datetime.utcnow() + timedelta(days=1),
        'iat':datetime.utcnow(),
        'sub': self.id
        }

        token = jwt.encode(
            payload,
            secret,
            'HS256'
        ).decode('utf-8')

        return token


class CommentUser(db.Model, BaseModel):

    __tablename__ = 'comments_user'

    content = db.Column(db.Text, nullable=False)
    user_comment_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys=[user_comment_id], backref='comments_user')
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    creator = db.relationship('User', foreign_keys=[creator_id], backref='created_comments')

class CommentUserSchema(ma.ModelSchema):

    creator = fields.Nested('UserSchema', only=('id', 'username'))
    user = fields.Nested('UserSchema', only=('id', 'username'))
    class Meta:
        model = CommentUser

class UserSchema(ma.ModelSchema, BaseSchema):

    @validates_schema
    #pylint:disable=R0201
    def check_passwords_match(self, data):
        if data.get('password') != data.get('password_confirmation'):
            raise ValidationError(
            'Passwords do not match',
            'password_confirmation'
        )

    password = fields.String(
    required=True,
    validate=[validate.Length(min=4, max=50)]
    )

    password_confirmation = fields.String(required=True)
    comments_user = fields.Nested('CommentUserSchema', many=True, exclude=('users'))
    designers = fields.Nested('DesignerSchema', many=True)
    creator = fields.Nested('UserSchema', only=('id', 'username'))
    liked_by = fields.Nested('UserSchema', many=True, only=('id', 'username'))
    created_designers = fields.Nested('DesignerSchema', many=True)
    likes = fields.Nested('ItemPostSchema', many=True, only=('id', 'name'))
    created_posts = fields.Nested('ItemPostSchema', many=True)


    class Meta:
        model = User
        exclude = ('password_hash', )
