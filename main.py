from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "sadfsdifaskdfadfs"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@127.0.0.1:3306/notas-app"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "usuarios.login"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_usuario(id):
        from models import Usuario
        return Usuario.query.get(int(id))



    from controlador_notas import notas
    from controlador_usuario import usuarios

    app.register_blueprint(usuarios, url_prefix="/usuarios")
    app.register_blueprint(notas, url_prefix="/notas")

    return app


if __name__ == "__main__":
    app = init_app()
    app.run(debug=True)


