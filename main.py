from src.core.dataset.Reader import Reader
from src.core.preprocessing.Preprocessor import Preprocessor
from src.config.settings import HAM_FOLDER,SPAM_FOLDER,PROCESSED_DATA_PATH
from src.core.dataset.DatasetManager import DatasetManager
from src.core.dataset.storage.CsvStorage import CsvStorage
if __name__ == "__main__": 
    reader = Reader()
    X,Y =reader.build_dataset_raw(HAM_FOLDER,SPAM_FOLDER)
    print(X[0])
    print(Y[0])
    print("*******************************************************************************************************")
    processor = Preprocessor()
    X_body = [processor.extract_mail_body(mail) for mail in X]
    X_processed= [processor.text_to_lowerCase(processor.replace_invalide_chars(mail)) for mail in X_body]
    
    csv_storage = CsvStorage(PROCESSED_DATA_PATH+"/dataset_cleaned.csv")
    dataset_manager = DatasetManager(csv_storage)
    dataset_manager.save(X_processed,Y)
    df =dataset_manager.load()
    print(df.count())