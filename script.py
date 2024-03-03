from cryptography.fernet import Fernet
import os
# from dotenv import load_dotenv

# load_dotenv('.env')

def decrypt_file(filename, key):
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(filename, "wb") as file:
        file.write(decrypted_data)

key = os.environ.get('ENK_KEY')
file = 'grade.py'

decrypt_file(file, key)