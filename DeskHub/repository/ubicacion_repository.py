from utils.db import db
from models.ubicacion import Ubicacion

class UbicacionRepository:
    def listar(self):
        return Ubicacion.query.all()

    def crear(self, nombre):
        nueva = Ubicacion(Nombre=nombre, EstadoUbicacion=1)  # siempre activa al crear
        db.session.add(nueva)
        db.session.commit()

    def editar(self, id, nombre):  
        ubicacion = Ubicacion.query.get(id)
        if ubicacion:
            ubicacion.Nombre = nombre
            db.session.commit()

    def eliminar(self, id):
        ubicacion = Ubicacion.query.get(id)
        if ubicacion:
            db.session.delete(ubicacion)
            db.session.commit()
