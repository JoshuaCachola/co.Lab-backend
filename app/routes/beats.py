import os
from flask import Blueprint, jsonify, request, send_file
from flask_cors import cross_origin
from ..storage import upload_file, list_files, download_file

bp = Blueprint('beats', __name__, url_prefix='/api/beats')

BEATS_FOLDER = 'beats'
BUCKET = 'colab-bucket-dev'


@bp.route('')
@cross_origin(headers=['Content-Type', 'Authorization'])
def get_beats():
    beats = list_files(BUCKET)
    return 

@bp.route('/<int:id>')
@cross_origin(headers=['Content-Type', 'Authorization'])
def get_a_beat():
    beat = download_file(filename, BUCKET)
    return send_file(output, as_attachment=True)


@bp.route('', methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def upload_beat():
    f = request.files['file']
    f.save(os.path.join(BEATS_FOLDER, f.filename))
    upload_file(f'beats/{f.filename}', BUCKET)
