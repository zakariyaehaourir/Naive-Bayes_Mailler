import pandas as pd
from .storage.DatasetStorage import DatasetStorage

class DatasetManager:
    def __init__(self,storage_type:DatasetStorage):
        self.storage = storage_type
    def save(self, X, y):
        self.storage.save(X, y)

    def load(self):
        return self.storage.load()
