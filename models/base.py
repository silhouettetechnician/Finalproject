from datetime import datetime
from marshmallow import fields
from app import db
# pylint: disable=E1101

class BaseModel:
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,
    default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
    default=datetime.utcnow)

    def save(self):
        self.updated_at = datetime.utcnow()

        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

class BaseSchema:
    created_at = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    updated_at = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
