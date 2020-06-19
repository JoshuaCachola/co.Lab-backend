from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from flask_login import current_user
from flask_cors import cross_origin
from ..models import db, User


bp = Blueprint('users', __name__, url_prefix='/api/users')


@bp.route('/signup', methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def sign_up():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        try:
            user = User(username=data['username'],
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        password=data['password'])
            db.session.add(user)
            db.session.commit()
            auth_token = user.encode_auth_token(user.id)
            responseObj = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
            }
            return make_response(jsonify(responseObj)), 201
        except Exception as e:
            responseObj = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObj)), 401
    else:
        responseObj = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return make_response(jsonify(responseObj)), 202


@bp.route('/login', methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def login():
    data = request.json
    try:
        user = User.query.filter_by(username=data['username']).first()
        auth_token = user.encode_auth_token(user.id)
        if auth_token:
            responseObj = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': auth_token.decode()
                }
            return make_response(jsonify(responseObject)), 200
    except Exception as e:
        print(e)
        responseObj = {
            'status': 'fail',
            'message': 'Please try again'
        }
        return make_response(jsonify(responseObj)), 500
