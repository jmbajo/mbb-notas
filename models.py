from main import db
from sqlalchemy.sql.functions import now

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)
    # TODO campos para almacenar información de login
    email = db.Column(db.String(300), unique=True)

    # notas = db.relationship("Nota")


class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500))
    fecha_creacion = db.Column(db.DateTime, default=now())
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))

    # usuario = db.relationship(Usuario)

