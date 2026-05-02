from flask import Blueprint, render_template,g
from .model import db, manga
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
  Manga = manga.query.get_or_404(id)
  return render_template("manga.html", manga=Manga)
@main.route("/adm")
def am():
    if not g.user:
        return render_template("login.html")
    if g.user.admin == True:
        return render_template("admin.html")
    else:
        print(g.user.email)
        return render_template("index.html")
    