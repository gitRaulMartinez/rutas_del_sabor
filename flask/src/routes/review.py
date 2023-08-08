from flask import Blueprint, jsonify, request, g
from src.auth.auth import auth
from src.models.review import Review

import src.controllers.review as reviewController
import src.controllers.culinaryDestination as culinaryDestinationController

import uuid

review_bp = Blueprint('review', __name__, url_prefix='/reviews')

# Registramos usuario
@review_bp.route('/create', methods=['POST'])
@auth
def create_review():
    new_review = request.json
    review_id = str(uuid.uuid4())
    user_id = g.user.get('_id')
    destination_id = new_review.get('culinary_destination_id')
    score = new_review.get('score')
    commment = new_review.get('comment')
    animo = new_review.get('animo')

    new_review = Review(review_id, destination_id, user_id, score, commment, animo)
    try:
        reviewController.addReview(new_review)
        reviews = [review.score for review in reviewController.getReviews() if review.culinary_destination_id == new_review.culinary_destination_id]
        culinaryDestinationController.updatePopularity(culinary_destination_id=new_review.culinary_destination_id,new_popularity=round(sum(reviews)/len(reviews)))
        return jsonify(new_review.__dict__), 200
    except Exception as e:
        return jsonify({'message': f'Error al agregar review {e}'}), 500

@review_bp.route('/', methods=['GET'])
def get_reviews():
    try:
        reviews = reviewController.getReviews()
        return jsonify([review.__dict__ for review in reviews]), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener rutas de visita {e}'}), 500