import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
SPAM_FOLDER = os.path.join(RAW_DATA_PATH, "spam")
HAM_FOLDER = os.path.join(RAW_DATA_PATH, "easy_ham")

PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed")
TEST_SIZE=0.2
RANDOME_STATE = 42

MODEL_PATH = os.path.join(BASE_DIR , "models")
MODEL_NAME = os.path.join(MODEL_PATH , "naive_baise.pkl")
VECTORIZER_NAME =os.path.join(MODEL_PATH , "vectorizer.pkl")

REAL_PREDICT = os.path.join(BASE_DIR  , "data" , "test")
REAL_SPAM = os.path.join(REAL_PREDICT , "spam.txt")
REAL_HAM = os.path.join(REAL_PREDICT , "ham.txt")