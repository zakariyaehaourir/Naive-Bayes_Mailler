from src.core.model.trainning.NaiveBaiseClassifier import NaiveBaiseClassifier
from src.core.dataset.Reader import Reader
from src.config.settings import MODEL_NAME,VECTORIZER_NAME
from src.core.preprocessing.Preprocessor import Preprocessor
from src.core.features.DefaultVectorizer import DefaultVectorizer
from src.core.model.trainning.Trainer import Trainer
class PredictionService:
    def __init__(self):
        trainer = Trainer(NaiveBaiseClassifier())
        trainer.load_model(MODEL_NAME)
        self.model = trainer.modal
        self.processor = Preprocessor()
        vec = DefaultVectorizer()
        vec.load_vectorizer(VECTORIZER_NAME)
        self.vectorizer = vec.count_vecotrizer
    
    def predict_real_world(self,mail_path:str):
        mail_content = Reader().get_file_content(mail_path)
        mail_content = self.processor.extract_mail_body(mail_content)
        mail_content = self.processor.replace_invalide_chars(mail_content)
        mail_content = self.processor.text_to_lowerCase(mail_content)

        mail_vectorized = self.vectorizer.transform([mail_content])

        label = self.model.predict(mail_vectorized)
        return label[0]
    