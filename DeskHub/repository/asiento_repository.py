from models.asiento import db, Asiento

class AsientoRepository:
    def listar(self):
        return Asiento.query.all()

    def leer(self, id_asiento):
        return Asiento.query.get(id_asiento)

    def crear(self, nombre, estado, id_ubicacion):
        asiento = Asiento(Nombre=nombre, EstadoAsiento=estado, IdUbicacion=id_ubicacion)
        db.session.add(asiento)
        db.session.commit()
        return asiento

    def actualizar(self, id_asiento, nombre, estado, id_ubicacion):
        asiento = Asiento.query.get(id_asiento)
        if asiento:
            asiento.Nombre = nombre
            asiento.EstadoAsiento = estado
            asiento.IdUbicacion = id_ubicacion
            db.session.commit()
        return asiento

    def eliminar(self, id_asiento):
        asiento = Asiento.query.get(id_asiento)
        if asiento:
            db.session.delete(asiento)
            db.session.commit()
            return True
        return False
