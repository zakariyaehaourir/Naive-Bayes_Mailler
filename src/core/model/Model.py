from abc import ABC,abstractmethod
class Model(ABC):
    @abstractmethod
    def train(X,Y):
        pass

    @abstractmethod
    def predict(X):
        pass

    @abstractmethod
    def save_model(path):
        pass
    
    @abstractmethod
    def load_model(path):
        pass