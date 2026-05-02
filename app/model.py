from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class manga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.String(300))
    capa = db.Column(db.String(200))
    capitulo = db.Column(db.Integer)
    genero = db.Column(db.String(100))
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)