from .DatasetStorage import DatasetStorage
import pandas as pd
class CsvStorage(DatasetStorage):
    def __init__(self, folder_path:str):
        self.folder_path=folder_path

    def save(self, X, Y):
        df = pd.DataFrame({"content": X, "label": Y})
        df.to_csv(self.folder_path, index=False)


    def load(self):
        return pd.read_csv(self.folder_path)
