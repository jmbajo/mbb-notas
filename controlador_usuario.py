import random

from flask import Blueprint, render_template, flash, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from models import Usuario, Nota
from flask_login import login_user, logout_user, login_required, current_user

usuarios = Blueprint("usuarios", __name__)

@usuarios.route("/", methods=["POST", "GET"])
@login_required
def home():
    if request.method == "POST":
        texto = request.form["texto"]
        if texto == " ":
            texto = "(Nota Vacia)"

        nueva_nota = Nota(texto=texto, usuario_id=current_user.id)

        from main import db
        db.session.add(nueva_nota)
        db.session.commit()

    return render_template('home.html', user=current_user)




@usuarios.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Validación y loguear (potencialmente) al usuario
        email = request.form["email"]
        passw = request.form["password"]

        user = Usuario.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, passw):
            flash("Usuario logueado")
            login_user(user, remember=True)
            return redirect(url_for("usuarios.home"))
        else:
            flash("Usuario o password incorrectos")
            return render_template("login.html")

    else:
        return render_template("login.html")


@usuarios.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("usuarios.login"))




@usuarios.route("/sign-up", methods=["GET", "POST"])
def alta_usuario():
    if request.method == "POST":
        # procesar el formulario y crear un nuevo usuario en la BD
        print(request.form)
        email = request.form["email"]
        nombre = request.form["firstName"]
        pass1 = request.form["password1"]
        pass2 = request.form["password2"]

        if pass1 != pass2:
            flash("Los passwords no coinciden.")
        elif email == "":
            flash("No se puede crear un usuario sin email.")
        else:
            from models import Usuario

            usuario = Usuario.query.filter_by(email=email).first()
            if usuario is not None:
                flash("Ese mail ya está registrado")
            else:
                nuevo_usuario = Usuario(nombre=nombre,
                                        email=email,
                                        password=generate_password_hash(pass1, method='sha256'))
                from main import db

                db.session.add(nuevo_usuario)
                db.session.commit()

                flash("Usuario Creado")
                login_user(nuevo_usuario, remember=True)
                return render_template("login.html")

    else:
        return render_template('sign_up.html')



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

