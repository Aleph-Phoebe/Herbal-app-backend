from flask import Blueprint, request, jsonify
from app.models import Favorite, Remedy
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

favorite_bp = Blueprint('favorite', __name__)

@favorite_bp.route('/favorites', methods=['POST'])
@jwt_required()
def add_favorite():
    user_id = get_jwt_identity()
    remedy_id = request.json['remedy_id']
    favorite = Favorite(user_id=user_id, remedy_id=remedy_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify({'message': 'Added to favorites.'}), 201

@favorite_bp.route('/favorites', methods=['GET'])
@jwt_required()
def get_favorites():
    user_id = get_jwt_identity()
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    return jsonify([favorite.remedy.serialize() for favorite in favorites])
