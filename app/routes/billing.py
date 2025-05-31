from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('billing', __name__, url_prefix='/billing')

@bp.route('/')
def billing_home():
    return render_template('billing.html')

@bp.route('/checkout', methods=['POST'])
def checkout():
    selected_plan = request.form.get('plan')
    return render_template('checkout.html', plan=selected_plan)
