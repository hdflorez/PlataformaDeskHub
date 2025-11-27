from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def ejecutar(self, *args, **kwargs):
        pass
