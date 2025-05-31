from flask import Blueprint, render_template

bp = Blueprint('da_health', __name__, url_prefix='/health')

@bp.route('/')
def index():
    return render_template('da_health.html')