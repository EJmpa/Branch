from flask import Blueprint
from app.routes import auth, messages, main  # noqa: E402

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
messages_bp = Blueprint('messages', __name__, url_prefix='/messages')
main_bp = Blueprint('main', __name__)


