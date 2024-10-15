from flask import Blueprint, jsonify
from .models import Herb

main = Blueprint('main', __name__)

@main.route('/herbs', methods=['GET'])
def get_herbs():
    herbs = Herb.query.all()
    return jsonify([{
        'id': herb.id,
        'name': herb.name,
        'advantages': herb.advantages,
        'image': herb.image,
        'comments': herb.comments
    } for herb in herbs])
