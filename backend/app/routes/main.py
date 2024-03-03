from flask import Blueprint, request, jsonify
from app.services.customer_service import update_customer_username

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "Hello, World!"

@main_bp.route('/home')
def return_json():
    return jsonify({"message": "Hello, World!"})

@main_bp.route('/customer/<int:customer_id>/update_username', methods=['POST'])
def update_customer_username_route(customer_id):
    data = request.get_json()
    new_username = data.get('username')

    if not new_username:
        return jsonify({'error': 'Invalid input'}), 400

    result = update_customer_username(customer_id, new_username)

    if result:
        return jsonify({'message': 'Username updated successfully'}), 200
    else:
        return jsonify({'error': 'Username update failed'}), 400