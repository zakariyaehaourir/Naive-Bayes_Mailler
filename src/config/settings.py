import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw")
SPAM_FOLDER = os.path.join(RAW_DATA_PATH, "spam")
HAM_FOLDER = os.path.join(RAW_DATA_PATH, "easy_ham")

PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed")
TEST_SIZE=0.2