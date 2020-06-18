from flask import Blueprint, request
from flask_login import current_user
from ..models import db, User


bp = Blueprint('session', __name__, url_prefix='/api/session')


@bp.route('', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return
    data = request.json
