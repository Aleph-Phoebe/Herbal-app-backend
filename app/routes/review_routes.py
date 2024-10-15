from flask import Blueprint, request, jsonify
from app.models import Review, Remedy
from app import db

review_bp = Blueprint('review', __name__)

@review_bp.route('/remedies/<int:id>/reviews', methods=['GET'])
def get_reviews(id):
    reviews = Review.query.filter_by(remedy_id=id).all()
    return jsonify([review.serialize() for review in reviews])

@review_bp.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    review = Review(user_id=data['user_id'], remedy_id=data['remedy_id'], rating=data['rating'], comment=data['comment'])
    db.session.add(review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully.'}), 201
