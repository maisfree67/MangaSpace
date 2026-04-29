from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
app = Flask(
    __name__,
    template_folder=os.path.join(os.getcwd(), "templates"),
    static_folder=os.path.join(os.getcwd(), "static")
)
db = SQLAlchemy()

def create_app():
    

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.secret_key = "segredo123"
    db.init_app(app)
    CORS(app)

    from .routes import main
    from .api import api
    from .auth import auth

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(auth)
    return app