from flask import jsonify, Blueprint, request
from app.model.review import db, Review

review = Blueprint('review', __name__)


@review.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    result = []
    for review in reviews:
        result.append(review_to_dict(review))
    return jsonify(result)


@review.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review_to_dict(review))


@review.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    review = Review(
        name=data['name'],
        rating=data['rating'],
        comment=data['comment']
    )
    db.session.add(review)
    db.session.commit()
    return jsonify(review_to_dict(review)), 201


@review.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    data = request.get_json()
    review.name = data['name']
    review.rating = data['rating']
    review.comment = data['comment']
    db.session.commit()
    return jsonify(review_to_dict(review))


@review.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted'})


def review_to_dict(review):
    return {
        'id': review.id,
        'name': review.name,
        'rating': review.rating,
        'comment': review.comment,
        'created_at': review.created_at,
        'updated_at': review.updated_at
    }