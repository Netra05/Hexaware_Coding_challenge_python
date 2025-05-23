# dao/i_adoptable.py

from abc import ABC, abstractmethod

class IAdoptable(ABC):
    @abstractmethod
    def adopt(self):
        pass
