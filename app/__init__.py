from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .model import db, user
import os



def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), "templates"),
        static_folder=os.path.join(os.getcwd(), "static")
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
   
    app.secret_key = "PauDuro13cm"
    db.init_app(app)
    CORS(app)
    @app.before_request
    def G():
        from flask import g
        if "usuario_id" in session:
            g.user = user.query.get(session["usuario_id"])
        else:
            g.user = None
    from .routes import main
    from .api import api
    from .auth import auth

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(auth)
    return app