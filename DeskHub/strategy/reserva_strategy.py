from .strategy_base import Strategy
from models.reserva import Reserva, db

class CrearReserva(Strategy):
    def ejecutar(self, usuario, fecha, asiento, jornada):
        nueva = Reserva(NombreUsuario=usuario, Fecha=fecha, IdAsiento=asiento, IdJornada=jornada)
        db.session.add(nueva)
        db.session.commit()
        return nueva

class CancelarReserva(Strategy):
    def ejecutar(self, id_reserva):
        reserva = Reserva.query.get(id_reserva)
        if reserva:
            db.session.delete(reserva)
            db.session.commit()
            return True
        return False
