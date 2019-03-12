#Dependency
pycryptodome==3.7.3

#Usage
1. pip install -r requirement.txt
2. create a text file, named "crypt_key", write a string as your crypt key into it. The key can not be longer than 32 characters.
3. modify "password_tools.py", update CRYPT_KEY_PATH to your crypt key path.
4. use "python password_tools.py -e <your_password>" to encrypt your password. use "python password_tools.py -d <encrypted_password>" to decrypt your password.
