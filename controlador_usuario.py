from flask import Blueprint


usuarios = Blueprint("usuarios", __name__)

@usuarios.route("/")
def home():
    return "Estoy en el home de usuarios"


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
    d4 = Nota(texto="d3", usuario_id=4)

    # db.session.add(u1)
    # db.session.add(u2)
    # db.session.add(u3)
    # db.session.add(d1)
    # db.session.add(d2)
    # db.session.add(d3)
    db.session.add(d4)

    db.session.commit()

