from . import db
from .asiento import Asiento
from .tipo_jornada import TipoJornada

class Reserva(db.Model):
    __tablename__ = "RESERVAS"

    IdReserva = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NombreUsuario = db.Column(db.String(100), nullable=False)
    Fecha = db.Column(db.Date, nullable=False)

    IdAsiento = db.Column(db.Integer, db.ForeignKey("ASIENTOS.IdAsiento"), nullable=False)
    IdJornada = db.Column(db.Integer, db.ForeignKey("TIPO_JORNADA.IdJornada"), nullable=False)

    asiento = db.relationship("Asiento", backref="reservas")
    jornada = db.relationship("TipoJornada", backref="reservas")
