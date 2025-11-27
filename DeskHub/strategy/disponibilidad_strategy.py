from .strategy_base import Strategy
from models.asiento import Asiento

class MarcarDisponible(Strategy):
    def ejecutar(self, asiento: Asiento):
        asiento.EstadoAsiento = True

class MarcarOcupado(Strategy):
    def ejecutar(self, asiento: Asiento):
        asiento.EstadoAsiento = False
