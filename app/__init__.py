from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py or .env
    app.config.from_object('app.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    CORS(app)  # Enable Cross-Origin Resource Sharing

    # Register routes (import routes here)
    from app.routes import main
    app.register_blueprint(main)

    return app
