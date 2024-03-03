from flask import Blueprint, request, jsonify
from app.services.auth_service import authenticate_customer, authenticate_agent, create_customer, create_agent
from app.utils.decorators import validate_json

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
@validate_json
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
        return jsonify({'error': 'Invalid input'}), 400

    customer = authenticate_customer(username, password)
    agent = authenticate_agent(username, password)

    if customer:
        return jsonify({'role': 'customer', 'message': 'Login successful'}), 200
    elif agent:
        return jsonify({'role': 'agent', 'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@auth_bp.route('/signup/customer', methods=['POST'])
@validate_json
def signup_customer():
    data = request.get_json()
    customer_name = data.get('customer_name')
    email = data.get('email')
    phone = data.get('phone')
    username = data.get('username')
    password = data.get('password')

    if not all([customer_name, email, phone, username, password]):
        return jsonify({'error': 'Invalid input'}), 400

    customer = create_customer(customer_name, email, phone, username, password)

    if customer:
        return jsonify({'role': 'customer', 'message': 'Account created successfully'}), 201
    else:
        return jsonify({'error': 'Account creation failed'}), 400

@auth_bp.route('/signup/agent', methods=['POST'])
@validate_json
def signup_agent():
    data = request.get_json()
    name = data.get('agent_name')
    username = data.get('username')
    password = data.get('password')

    if not all([name, username, password]):
        return jsonify({'error': 'Invalid input'}), 400

    agent = create_agent(name, username, password)

    if agent:
        return jsonify({'role': 'agent', 'message': 'Account created successfully'}), 201
    else:
        return jsonify({'error': 'Account creation failed'}), 400