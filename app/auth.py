from .model import db, user
from flask import Blueprint, request, render_template, session

auth = Blueprint("auth", __name__)
auth.secret_key = "PauDuro13cm" #senha do baguio

@auth.route("/RD1", methods=["POST"])
def RD2(): # registro 
    if request.method == "POST": # pegando os dados do form
        name = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha") 
        if email:
            if user.query.filter_by(email = email).first(): # verificando se o email esta sendo usado
                return render_template("login.html", erro="Email ja usado")
            Salve = user(nome = name, email = email, senha = senha)
            db.session.add(Salve)
            db.session.commit()
            print(email)
            return render_template("login.html") # volta para a tela de login
        return "error"
@auth.route("/LD1", methods=["POST"])
def LD2():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        if email:
            if senha:
                User = user.query.filter_by(email= email, senha= senha).first()
                if User:
                    session['usuario_id'] = User.id #salva o usuario e inicia a sessao
                    if User.email == "noutia@gmail.com":
                        User.admin = True
                        db.session.commit()
                    return render_template("index.html")
                else:
                    return render_template("login.html", erro="Senha ou Email incorreta")
