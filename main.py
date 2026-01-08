from src.core.dataset.Reader import Reader
from src.core.preprocessing.Preprocessor import Preprocessor
from src.config.settings import HAM_FOLDER,SPAM_FOLDER,PROCESSED_DATA_PATH
from src.core.dataset.DatasetManager import DatasetManager
from src.core.dataset.storage.CsvStorage import CsvStorage
from src.core.features.VectorizeManager import VectorizeManager
from src.core.features.DefaultVectorizer import DefaultVectorizer
from sklearn.model_selection import train_test_split
from src.config.settings import TEST_SIZE,RANDOME_STATE
from src.core.model.Model import Model
from src.core.model.trainning.NaiveBaiseClassifier import NaiveBaiseClassifier
from src.core.model.Spliter import Spliter
from src.core.model.trainning.Trainer import Trainer
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
    #dataset_manager.save(X_processed,Y)
    df =dataset_manager.load()

    print(f"Number of spam : " , df['label'].value_counts()[1])
    print(f"Number of ham : " , df['label'].value_counts()[0])
    count_vectorizer =DefaultVectorizer()
    vac_manager =VectorizeManager(count_vectorizer)
    vac_manager.build_vocabulary(df['content'])
    z=vac_manager.get_vocabulary()
    #print(z)
    X_vect = vac_manager.transform(X)
    naive_baise = NaiveBaiseClassifier()
    trainer = Trainer(naive_baise)
    spliter = Spliter()
    X_train,X_test,Y_train,Y_test = spliter.split_dataset(X_vect , Y , TEST_SIZE=TEST_SIZE , random=RANDOME_STATE)
    print(X_train.shape) #(nbr_emails en train , nbr features words vocabulary)
    trainer.train_model(X_train , Y_train)
