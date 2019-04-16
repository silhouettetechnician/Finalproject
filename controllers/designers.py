from flask import Blueprint
from models.designer import Designer, DesignerSchema

api = Blueprint('designers', __name__)

designers_schema = DesignerSchema()

@api.route('/designers', methods=['GET'])
def index():
    designers = Designer.query.all()

    return designers_schema.jsonify(designers, many=True), 200
