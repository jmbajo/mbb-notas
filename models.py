from main import db
from sqlalchemy.sql.functions import now
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(300), unique=True)

    notas = db.relationship("Nota")


class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500))
    fecha_creacion = db.Column(db.DateTime, default=now())
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))

    usuario = db.relationship(Usuario)

