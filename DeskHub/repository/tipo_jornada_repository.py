from models.tipo_jornada import db, TipoJornada

class TipoJornadaRepository:
    def listar(self):
        return TipoJornada.query.all()

    def leer(self, id_TipoJornada):
        return TipoJornada.query.get(id_TipoJornada)

    def crear(self, nombre):
        TipoJornada = TipoJornada(Nombre=nombre)
        db.session.add(TipoJornada)
        db.session.commit()
        return TipoJornada

    def actualizar(self, id_TipoJornada, nombre):
        TipoJornada = TipoJornada.query.get(id_TipoJornada)
        if TipoJornada:
            TipoJornada.Nombre = nombre
            db.session.commit()
        return TipoJornada

    def eliminar(self, id_TipoJornada):
        TipoJornada = TipoJornada.query.get(id_TipoJornada)
        if TipoJornada:
            db.session.delete(TipoJornada)
            db.session.commit()
            return True
        return False
