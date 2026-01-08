from sklearn.metrics import accuracy_score,confusion_matrix,f1_score,precision_score,recall_score
class Evaluator:
    def __init__(self,Y_test,Y_predir):
        self.Y_true=Y_test
        self.Y_pred = Y_predir

    def evaluate(self):
        return accuracy_score(self.Y_true , self.Y_pred)
    
    def confusion_matrix(self):
        return confusion_matrix(self.Y_true, self.Y_pred)


        """  
            when i said spam how many they are realy spam
            precision = TP /(TP+FP)
        """
    def precission(self):
        return precision_score(self.Y_true , self.Y_pred)

        """
            bassed on spams how many i said correctly spam
        """
    def recall(self):
        return recall_score(self.Y_true ,self.Y_pred)
        """

        """
    def f1_score(self):
        return f1_score(self.Y_true , self.Y_pred)
