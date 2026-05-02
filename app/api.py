from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .model import db, manga, user

api = Blueprint("api", __name__)

def convertM(manga):
    return {
        "id": manga.id,
        "titulo": manga.titulo,
        "descricao": manga.descricao,
        "capa": manga.capa,
        "capitulo": manga.capitulo,
        "genero": manga.genero,
    }
def convertU(usuario):
    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
    }
@api.route("/manga", methods=["GET"])
def Busca():
    search = request.args.get("q", "")
    genre = request.args.get("genre", "")
    id = request.args.get("id", "")

    busca = manga.query

    if search:
        busca = busca.filter(manga.titulo.ilike(f"%{search}%"))
    if genre:
        busca = busca.filter(manga.genero == genre)
    if id:
        busca = busca.filter(manga.id == id)
    mangas = busca.all()
    return jsonify([convertM(m) for m in mangas])
@api.route("/user", methods=["GET"])
def Bu():
    nome = request.args.get("nome", "")
    email = request.args.get("email", "")
    id = request.args.get("id", "")
    
    Busca = user.query

    if nome:
        Busca = Busca.filter(user.nome)
    if email:
        Busca = Busca.filter(user.email)
    if id:
        Busca = Busca.filter(user.id)
    usuario = Busca.all()
    return jsonify([convertU(u) for u in usuario])
    