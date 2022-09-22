from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controlador_notas import notas
from controlador_usuario import usuarios

app = Flask(__name__)
app.config["SECRET_KEY"] = "sadfsdifaskdfadfs"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@127.0.0.1:3306/notas-app"

db = SQLAlchemy(app)

app.register_blueprint(usuarios, url_prefix="/usuarios")
app.register_blueprint(notas, url_prefix="/notas")


if __name__ == "__main__":
    app.run(debug=True)


