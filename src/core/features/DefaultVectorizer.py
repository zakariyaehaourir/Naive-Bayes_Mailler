from .Vectorizer import Vectorizer
from sklearn.feature_extraction.text import CountVectorizer

import joblib
class DefaultVectorizer(Vectorizer):
    def __init__(self):
        self.count_vecotrizer = CountVectorizer(stop_words="english")
    

    """
        Matrice counting , count each occurence of word in the vocabulary generated with set_vocabulary()
       Transform each content to a numeric vector
    """
    def transform(self ,X): 
        return self.count_vecotrizer.transform(X)
    

    """
        Define a list of vocabulary depending on the content of emails
    """
    def set_vocabulary(self ,X): #construct vocabulary list #X_feature
        self.count_vecotrizer.fit(X)
    

    """
        Shortcut that combine set_voca and transform
    """
    def fit_transform(self ,X):
        return self.count_vecotrizer.fit_transform(X) 
    

    def get_vocabulary(self):
        return self.count_vecotrizer.vocabulary_

    def save_vectorizer(self , path):
        joblib.dump(self.count_vecotrizer , path)
    
    def load_vectorizer(self , path):
        self.count_vecotrizer = joblib.load(path)