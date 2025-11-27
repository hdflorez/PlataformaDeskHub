from models.reserva import db, Reserva

class ReservaRepository:
    def listar(self):
        return Reserva.query.all()

    def leer(self, id_Reserva):
        return Reserva.query.get(id_Reserva)

    def crear(self, nombre):
        Reserva = Reserva(Nombre=nombre)
        db.session.add(Reserva)
        db.session.commit()
        return Reserva

    def actualizar(self, id_Reserva, nombre):
        Reserva = Reserva.query.get(id_Reserva)
        if Reserva:
            Reserva.Nombre = nombre
            db.session.commit()
        return Reserva

    def eliminar(self, id_Reserva):
        Reserva = Reserva.query.get(id_Reserva)
        if Reserva:
            db.session.delete(Reserva)
            db.session.commit()
            return True
        return False
