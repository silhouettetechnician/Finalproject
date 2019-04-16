from app import db, ma
from marshmallow import fields
from .base import BaseModel

class Designer(db.Model, BaseModel):

    __tablename__ = 'designers'
 # pylint: disable=E1101
    name = db.Column(db.String(40), unique=True,
    nullable=False)
    image = db.Column(db.String(500))


class DesignerSchema(ma.ModelSchema):

    item_post = fields.Nested('ItemPostSchema', many=True,
    exclude=('designers',))

    class Meta:
        model = Designer
