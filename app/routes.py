from flask import Blueprint, render_template
from .model import db, Manga
main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")
@main.route("/E1")
def explorar():
    return render_template("explora.html")

@main.route("/L1")
def login():
    return render_template("login.html")
@main.route("/manga/<int:id>")
def ler(id):
  manga = Manga.query.get_or_404(id)
  return render_template("manga.html", manga=manga) 
