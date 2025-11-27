from flask import Flask, render_template, request, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

from utils.db import db
from models.usuario import Usuario
from models.ubicacion import Ubicacion
from repository.usuario_repository import UsuarioRepository
from repository.ubicacion_repository import UbicacionRepository

# ------------------- CONFIG -------------------
load_dotenv()  # lee las variables de .env

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY", "super_secret_key")  # Necesario para CSRF/State

# Conexión a SQL Server
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mssql+pyodbc://DESKTOP-H0QG9UU\SQLEXPRESS/DESKHUB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Auth0
oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=os.getenv("AUTH0_CLIENT_ID"),
    client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
    client_kwargs={"scope": "openid profile email"},
    server_metadata_url=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

# Repositorios
usuario_repo = UsuarioRepository()
ubicacion_repo = UbicacionRepository()

# ------------------- LOGIN FLOW -------------------

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback")
def callback():
    token = oauth.auth0.authorize_access_token()  # 🔹 Aquí fallaba sin secret_key
    session["user"] = token["userinfo"]
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ------------------- RUTAS -------------------

@app.route("/")
def index():
    # 🔹 Si no hay sesión → mandar al login
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", user=session["user"])

# ------------------- USUARIOS -------------------

@app.route("/usuarios")
def usuarios():
    if "user" not in session:
        return redirect(url_for("login"))
    lista = usuario_repo.listar()
    return render_template("usuarios.html", usuarios=lista)

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    tipo = request.form["tipo_usuario"]
    identificacion = request.form["identificacion"]
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    usuario_repo.crear(tipo, identificacion, nombre, correo)
    return redirect(url_for("usuarios"))

@app.route("/usuarios/editar/<int:id>", methods=["GET", "POST"])
def editar_usuario(id):
    if "user" not in session:
        return redirect(url_for("login"))
    usuario = Usuario.query.get(id)
    if request.method == "POST":
        usuario.TipoUsuario = request.form["tipo_usuario"]
        usuario.Identificacion = request.form["identificacion"]
        usuario.Nombre = request.form["nombre"]
        usuario.correo = request.form["correo"]
        db.session.commit()
        return redirect(url_for("usuarios"))
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/usuarios/inactivar/<int:id>", methods=["POST"])
def inactivar_usuario(id):
    usuario_repo.inactivar(id)
    return redirect(url_for("usuarios"))

# ------------------- UBICACIONES -------------------

@app.route("/ubicaciones")
def ubicaciones():
    if "user" not in session:
        return redirect(url_for("login"))
    lista = ubicacion_repo.listar()
    return render_template("ubicaciones.html", ubicaciones=lista)

@app.route("/ubicaciones/crear", methods=["POST"])
def crear_ubicacion():
    nombre = request.form["nombre"]
    ubicacion_repo.crear(nombre)
    return redirect(url_for("ubicaciones"))

@app.route("/ubicaciones/editar/<int:id>", methods=["GET", "POST"])
def editar_ubicacion(id):
    if "user" not in session:
        return redirect(url_for("login"))
    ubicacion = Ubicacion.query.get(id)
    if request.method == "POST":
        nombre = request.form["nombre"]
        ubicacion_repo.editar(id, nombre)
        return redirect(url_for("ubicaciones"))
    return render_template("editar_ubicacion.html", ubicacion=ubicacion)

@app.route("/ubicaciones/eliminar/<int:id>", methods=["POST"])
def eliminar_ubicacion(id):
    ubicacion_repo.eliminar(id)
    return redirect(url_for("ubicaciones"))

# ------------------- MAIN -------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)