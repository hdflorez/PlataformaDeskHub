from . import db
from .ubicacion import Ubicacion

class Asiento(db.Model):
    __tablename__ = "ASIENTOS"

    IdAsiento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(100), nullable=False)
    EstadoAsiento = db.Column(db.Boolean, nullable=False, default=True)
    IdUbicacion = db.Column(db.Integer, db.ForeignKey("UBICACION.IdUbicacion"), nullable=False)

    ubicacion = db.relationship("Ubicacion", backref="asientos")
