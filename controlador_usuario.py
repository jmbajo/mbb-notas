import random

from flask import Blueprint, render_template, flash


usuarios = Blueprint("usuarios", __name__)

@usuarios.route("/")
def home():
    return render_template("index.html")

@usuarios.route("/login")
def login():
    # simular que la mitad el login da incorrecto
    if random.randint(0,1) > 0:
        flash("el usuario se logueó correctamente", "success")
    else:
        flash("login incorrecto", "error")

    return render_template("login.html")


@usuarios.route("/cargar-datos")
def test():
    from main import db

    from models import Usuario
    from models import Nota

    # u1 = Usuario(nombre="A")
    # u2 = Usuario(nombre="B")
    # u3 = Usuario(nombre="C")
    u4 = Usuario(nombre="D")

    # d1 = Nota(texto="d1", usuario=u1)
    # d2 = Nota(texto="d2", usuario=u1)
    # d3 = Nota(texto="d3", usuario=u3)
    d4 = Nota(texto="d3", usuario=u4)

    # db.session.add(u1)
    # db.session.add(u2)
    # db.session.add(u3)
    # db.session.add(d1)
    # db.session.add(d2)
    # db.session.add(d3)
    db.session.add(d4)

    db.session.commit()

