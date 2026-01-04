from abc import ABC, abstractmethod
class DatasetStorage(ABC):
    @abstractmethod
    def save(self , X , Y):
        pass
    @abstractmethod
    def load(self):
        pass