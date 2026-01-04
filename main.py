from src.core.dataset.Reader import Reader
from src.config.settings import HAM_FOLDER,SPAM_FOLDER
if __name__ == "__main__": 
    reader = Reader()
    X,Y =reader.build_dataset_raw(HAM_FOLDER,SPAM_FOLDER)
    print(X[0])
    print(Y[0])