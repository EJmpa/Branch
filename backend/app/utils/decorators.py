from functools import wraps
from flask import request, jsonify

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.method == 'POST' or request.method == 'PUT':
            if not request.is_json:
                return jsonify({'error': 'Invalid JSON format'}), 400
        return f(*args, **kwargs)
    return wrapper
