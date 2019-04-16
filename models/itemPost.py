from app import db, ma
from marshmallow import fields
# pylint: disable=E1101, W0611
from models.designer import Designer
from models.category import Category
from .user import User, UserSchema
from .base import BaseModel

likes = db.Table(
'likes',
    db.Column('itemPost_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

designers_item_posts = db.Table('designers_ItemPosts',
    db.Column('designer_id', db.Integer, db.ForeignKey('designers.id'),
    primary_key=True),
    db.Column('itemPost_id', db.Integer, db.ForeignKey('posts.id'),
    primary_key=True)
)

categories_ItemPosts = db.Table('categories_ItemPosts',
    db.Column('itemPost_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)

class ItemPost(db.Model, BaseModel):

    __tablename__ = 'posts'

    title = db.Column(db.String(2000), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    size = db.Column(db.String(1000), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    image1 = db.Column(db.String(3000))
    image2 = db.Column(db.String(3000))
    image3 = db.Column(db.String(3000))
    creator = db.relationship('User', backref='created_posts')
    categories = db.relationship('Category', secondary=categories_ItemPosts, backref='categories')
    designers = db.relationship('Designer', secondary=designers_item_posts, backref='designers')
    liked_by = db.relationship('User', secondary=likes, backref='likes')

class ItemPostSchema(ma.ModelSchema):

    class Meta:
        model = ItemPost

    creator = fields.Nested('UserSchema', only=('id', 'username', 'image'))
    comments = fields.Nested('CommentSchema', many=True, exclude=('itemPost'))
    designers = fields.Nested('DesignerSchema', many=True)
    categories = fields.Nested('CategorySchema', many=True, only=('id', 'name'))
    liked_by = fields.Nested('UserSchema', many=True, only=('id', 'username'))


class Comment(db.Model, BaseModel):

    __tablename__ = 'comments'

    content = db.Column(db.Text, nullable=False)
    itemPost_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    itemPost = db.relationship('ItemPost', backref='comments')

class CommentSchema(ma.ModelSchema):

    class Meta:
        model = Comment
