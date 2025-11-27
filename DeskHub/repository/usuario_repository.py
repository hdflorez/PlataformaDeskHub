from utils.db import db
from models.usuario import Usuario

class UsuarioRepository:
    def listar(self):
        return Usuario.query.filter_by(EstadoUsuario=1).all()

    def crear(self, tipo_usuario, identificacion, nombre, correo):
        nuevo = Usuario(
            TipoUsuario=tipo_usuario,
            Identificacion=identificacion,
            Nombre=nombre,
            correo=correo,
            EstadoUsuario=1  # siempre activo al crear
        )
        db.session.add(nuevo)
        db.session.commit()

    def editar(self, id, tipo_usuario, identificacion, nombre, correo):
        usuario = Usuario.query.get(id)
        if usuario:
            usuario.TipoUsuario = tipo_usuario
            usuario.Identificacion = identificacion
            usuario.Nombre = nombre
            usuario.correo = correo
            db.session.commit()

    def inactivar(self, id): 
        usuario = Usuario.query.get(id)
        if usuario:
            usuario.EstadoUsuario = 0
            db.session.commit()
