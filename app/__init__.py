from flask_restx import Api
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env="dev"):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env])
    
    db = SQLAlchemy(app)
    
    api = Api(app, title="Queshi API ", version="0.1.0")

    register_routes(api, app, root="api")

    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app