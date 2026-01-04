from src.core.dataset.Reader import Reader
from src.core.preprocessing.Preprocessor import Preprocessor
from src.config.settings import HAM_FOLDER,SPAM_FOLDER
if __name__ == "__main__": 
    reader = Reader()
    X,Y =reader.build_dataset_raw(HAM_FOLDER,SPAM_FOLDER)
    print(X[0])
    print(Y[0])
    print("*******************************************************************************************************")
    processor = Preprocessor()
    X_body = [processor.extract_mail_body(mail) for mail in X]
    X_processed= [processor.text_to_lowerCase(processor.replace_invalide_chars(mail)) for mail in X_body]
