from flask import Blueprint, render_template

bp = Blueprint('da_education', __name__, url_prefix='/education')

@bp.route('/')
def index():
    return render_template('da_education.html')