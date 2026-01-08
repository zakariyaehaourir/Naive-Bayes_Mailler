from abc import ABC, abstractmethod
class Vectorizer(ABC):

    @abstractmethod
    def transform(self,X): 
        pass

    @abstractmethod
    def set_vocabulary(self,X): #construct vocabulary list #X_feature
        pass

    @abstractmethod
    def get_vocabulary(self):
        pass

    @abstractmethod
    def save_vectorizer(self, path):
        pass

    @abstractmethod
    def load_vectorizer(self , path):
        pass