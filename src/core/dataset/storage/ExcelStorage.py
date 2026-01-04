from .DatasetStorage import DatasetStorage
import pandas as pd
class ExcelStorage(DatasetStorage):
    def __init__(self,folder_path:str):
        self.folder_path = folder_path
    def save(self, X, Y):
        df = pd.DataFrame({"content": X, "label": Y})
        df.to_excel(self.folder_path, index=False)
    
    def load(self):
        df = pd.read_excel(self.folder_path)
        return df