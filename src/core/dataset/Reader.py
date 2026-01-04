import os
class Reader:
    """
        Summary:
            Iterates through the files in the specified directory to store thier names
        Args:
            path (str): Path to the directory containing files.
            label (int): Integer label to associate with each file (0 for ham, 1 for spam).
        Returns:
            list[tuple[str, int]]: A list of tuples where each tuple contains:
    """
    def read_files_from_directory(self ,path,label):
        data=[]
        files_names = os.listdir(path)
        
        for file_name in files_names:
            data.append((os.path.join(path,file_name),label))
        return data
    """
        Summary:
            Opens the file in read mode with UTF-8 encoding and returns its content.
        Args:
            path (str): Path to the file to be read.

        Returns:
            str: The full content of the file as a string.
    """
    def get_file_content(self ,path):
        with open(path , "r", encoding="utf-8" , errors="replace") as f:
            return f.read()
    """
        Summary:
            Reads files from both ham and spam directories, extracts their full content,
            and builds two lists:
                - X: containing the text content of each file
                - Y: containing the associated labels (0 for ham, 1 for spam).
        Args:
            ham_path (str): Path to the directory containing ham files.
            spam_path (str): Path to the directory containing spam files.

        Returns:
            tuple[list[str], list[int]]:
    """
    def build_dataset_raw(self , ham_path , spam_path):
        no_spam_files_name=self.read_files_from_directory(ham_path,0)
        spam_files_name = self.read_files_from_directory(spam_path,1)
        #(X , Y)
        X=[]
        Y=[]
        for file_name , label in no_spam_files_name:
            X.append(self.get_file_content(file_name))
            Y.append(label)
        
        for file_name , label in spam_files_name:
            X.append(self.get_file_content(file_name))
            Y.append(label)
   
        return X,Y