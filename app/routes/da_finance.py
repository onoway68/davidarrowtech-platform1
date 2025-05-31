from flask import Blueprint, render_template

bp = Blueprint('da_finance', __name__, url_prefix='/finance')

@bp.route('/')
def index():
    return render_template('da_finance.html')