from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/')
def entry_point():
    return 'Hello World'
