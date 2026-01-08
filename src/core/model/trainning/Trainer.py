from src.core.model.Model  import Model
class Trainer:
    def __init__(self, model:Model):
        self.modal = model
    
    def save_model(self,path):
        self.modal.save_model(path)

    def train_model(self , X , Y):
        self.modal.train(X,Y)
    
    def get_predict(self,X_test):
        return self.modal.predict(X_test)
    
    def load_model(self , path):
        self.modal.load_model(path)