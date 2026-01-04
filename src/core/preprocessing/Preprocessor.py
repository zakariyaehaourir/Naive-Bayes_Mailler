class Preprocessor:
    def extract_mail_body(self ,content:str):
        if "\n\n" in content:    
            headers,body = content.split("\n\n" , 1)
        elif "\r\n\r\n" in content:
            headers , body = content.split("\r\n\r\n", 1)
        else:
            body = content
        return body.strip()
        
    def replace_invalide_chars(self , email:str):
        return email.replace("�", " ")
    def text_to_lowerCase(self , email:str):
        return email.lower()