import pickle
from .DatasetStorage import DatasetStorage
class PickleStorage(DatasetStorage):
    def __init__(self, path):
        self.path = path

    def save(self, X, y):
        with open(self.path, "wb") as f:
            pickle.dump((X, y), f)

    def load(self):
        with open(self.path, "rb") as f:
            return pickle.load(f)
