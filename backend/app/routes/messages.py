from flask import Blueprint, request, jsonify
from app.services.message_service import send_message, get_messages, delete_message, respond_to_message, update_message
from app.utils.decorators import validate_json

messages_bp = Blueprint('messages', __name__, url_prefix='/messages')

@messages_bp.route('/send', methods=['POST'])
@validate_json
def send():
    data = request.get_json()
    customer_id = data.get('customer_id')
    agent_id = data.get('agent_id')
    content = data.get('content')

    if not all([customer_id, agent_id, content]):
        return jsonify({'error': 'Invalid input'}), 400

    new_message = send_message(customer_id, agent_id, content)

    if new_message is None:
        return jsonify({'error': 'Message sending failed'}), 400

    return jsonify({'message': 'Message sent successfully', 'message_id': new_message.message_id}), 200

@messages_bp.route('/respond', methods=['POST'])
@validate_json
def respond():
    data = request.get_json()
    agent_id = data.get('agent_id')
    message_id = data.get('message_id')
    content = data.get('content')

    if not all([agent_id, message_id, content]):
        return jsonify({'error': 'Invalid input'}), 400

    new_response = respond_to_message(agent_id, message_id, content)

    if new_response is None:
        return jsonify({'error': 'Invalid agent_id or message_id'}), 400

    return jsonify({'message': 'Response sent successfully', 'response_id': new_response.message_id}), 200

@messages_bp.route('/customer/<int:customer_id>/agent/<int:agent_id>', methods=['GET'])
def fetch_messages(customer_id, agent_id):
    messages = get_messages(customer_id, agent_id)

    if messages is None:
        return jsonify({'error': 'No messages found'}), 400

    return jsonify({'messages': [message.to_dict() for message in messages]}), 200

@messages_bp.route('/<int:message_id>', methods=['PUT'])
@validate_json
def update_message_route(message_id):
    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({'error': 'Invalid input'}), 400

    result = update_message(message_id, content)

    if result:
        return jsonify({'message': 'Message updated successfully'}), 200
    else:
        return jsonify({'error': 'Message update failed'}), 400

@messages_bp.route('/<int:message_id>', methods=['DELETE'])
def delete_message_route(message_id):
    result = delete_message(message_id)
    if result:
        return jsonify({'message': 'Message deleted successfully'}), 200
    else:
        return jsonify({'error': 'Message deletion failed'}), 400