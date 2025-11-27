from utils.db import db

class Ubicacion(db.Model):
    __tablename__ = "UBICACION"

    IdUbicacion = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    EstadoUbicacion = db.Column(db.Integer, nullable=False, default=1)   
