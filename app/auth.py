from .model import db, User
from flask import Blueprint, request, render_template

auth = Blueprint("auth", __name__)

@auth.route("/RD1", methods=["POST"])
def RD2():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        senha = request.form.get("senha")
        if email:
            if User.query.filter_by(email = email).first():
                return render_template("login.html", erro="Email ja usado")
            Salve = User(nome=name, email = email, senha = senha)
            db.session.add(Salve)
            db.session.commit()
            print(email)
            return "login enviado"
        return "error"
@auth.route("/LD1", methods=["POST"])
def LD2():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        if email:
            if senha:
                user = User.query.filter_by(email= email, senha= senha).first()
                if user:
                    return render_template("index.html")
                else:
                    return render_template("login.html", erro="Senha ou Email incorreto")