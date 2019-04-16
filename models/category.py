from app import db, ma
from marshmallow import fields
from .base import BaseModel

# pylint: disable=E1101
class Category(db.Model, BaseModel):

    __tablename__ = 'categories'

    name = db.Column(db.String(40), unique=True, nullable=False)

class CategorySchema(ma.ModelSchema):
    item_post = fields.Nested('ItemPostSchema', many=True, exclude=('categories',))

    class Meta:

        model = Category
        # we now need to bnuild the join table, we do this in our planet model
