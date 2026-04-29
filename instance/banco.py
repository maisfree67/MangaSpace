from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CONFIG DO BANCO
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class Manga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.String(300))
    capa = db.Column(db.String(200))
    capitulo = db.Column(db.Integer)
    genero = db.Column(db.String(100))
with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)
