from . import db

class TipoJornada(db.Model):
    __tablename__ = "TIPO_JORNADA"

    IdJornada = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombre = db.Column(db.String(100), nullable=False)
