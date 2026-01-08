from sklearn.model_selection import train_test_split

class Spliter:
    def __init__(self):
        pass

    def split_dataset(self ,X_vect , Y , random,TEST_SIZE=0.2 ):
           return train_test_split(X_vect, Y , test_size=TEST_SIZE,random_state=random,shuffle=True,stratify=Y)

