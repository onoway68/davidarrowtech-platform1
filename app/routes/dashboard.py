from flask import Blueprint, render_template
import json
from pathlib import Path

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dashboard_home():
    logs_path = Path(__file__).resolve().parent.parent / 'dashboard' / 'usage_logs.json'
    if logs_path.exists():
        with open(logs_path) as f:
            logs = json.load(f)
    else:
        logs = []

    return render_template('dashboard.html', logs=logs)
