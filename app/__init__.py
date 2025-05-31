from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import home, da_health, da_finance, da_education
    app.register_blueprint(home.bp)
    app.register_blueprint(da_health.bp)
    app.register_blueprint(da_finance.bp)
    app.register_blueprint(da_education.bp)

    return app