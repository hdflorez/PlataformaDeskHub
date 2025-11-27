from utils.db import db

class Usuario(db.Model):
    __tablename__ = "USUARIOS"

    IdUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TipoUsuario = db.Column(db.String(50), nullable=False)
    Identificacion = db.Column(db.String(50), nullable=False)
    Nombre = db.Column(db.String(500), nullable=False)
    correo = db.Column(db.String(1000), nullable=False)
    EstadoUsuario = db.Column(db.Boolean, nullable=False, default=True)  # 1 activo, 0 inactivo
