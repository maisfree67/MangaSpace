from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .model import db, Manga

api = Blueprint("api", __name__)

def convert(manga):
    return {
        "id": manga.id,
        "titulo": manga.titulo,
        "descricao": manga.descricao,
        "capa": manga.capa,
        "capitulo": manga.capitulo,
        "genero": manga.genero,
    }
@api.route("/manga", methods=["GET"])
def Busca():
    search = request.args.get("q", "")
    genre = request.args.get("genre", "")
    id = request.args.get("id", "")

    busca = Manga.query

    if search:
        busca = busca.filter(Manga.titulo.ilike(f"%{search}%"))
    if genre:
        busca = busca.filter(Manga.genero == genre)
    if id:
        busca = busca.filter(Manga.id == id)
    mangas = busca.all()
    return jsonify([convert(m) for m in mangas])