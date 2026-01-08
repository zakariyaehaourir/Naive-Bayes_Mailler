from .Vectorizer import Vectorizer
class VectorizeManager:
    def __init__(self, vect:Vectorizer):
        self.vectorizer = vect

    def transform(self,X):
        return self.vectorizer.transform(X)
    
    def build_vocabulary(self,X):
        self.vectorizer.set_vocabulary(X)

    def get_vocabulary(self):
        return self.vectorizer.get_vocabulary()