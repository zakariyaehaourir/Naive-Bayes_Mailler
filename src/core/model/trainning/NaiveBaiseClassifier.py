from src.core.model.Model import Model
from src.core.features.DefaultVectorizer import DefaultVectorizer
from src.core.features.Vectorizer import Vectorizer


from sklearn.naive_bayes import MultinomialNB
class NaiveBaiseClassifier(Model):
    def __init__(self):
        self.model =MultinomialNB()

    
    def train(self,X_train,Y_train):
        
        self.model.fit(X_train , Y_train)

    
    def save_model(self,path):
        pass
    
    def predict(self,X_test):
        return self.model.predict(X_test)