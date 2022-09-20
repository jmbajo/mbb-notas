
from flask import Blueprint

notas = Blueprint("notas", __name__)

@notas.route("/")
def home():
    return "Estoy en el home de NOTAS"


@notas.route("/test")
def test():
    return "Estoy en TEST de NOTAS"





