from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

import os
def cn():
    i=0
    n=str(i+1)+".txt"
    return n
def DAES(key,iv):
    n=cn()
    f=open(os.path.join(os.getcwd()+"/Parts",n),"rb")
    content=f.read()
    f.close()
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    content=decryptor.update(content) + decryptor.finalize()
    f=open(os.path.join(os.getcwd()+"/Parts",n),"wb")
    f.write(content)
    f.close()
    

def DeCryptKeys():
    f=open('Secured.txt','rb')
    key=f.read()
    f.close()
    fer = Fernet(key)
    listDir=os.listdir(os.path.join(os.getcwd(),"Keys_IV"))
    for i in listDir:
        path=os.path.join(os.getcwd()+"/Keys_IV",i)
        print(path)
        k=open(path,"rb")
        content=k.read()
        print(content)
        k.close()
        content=fer.decrypt(content)
        open(os.path.join(os.getcwd()+"/Keys_IV",i),"wb").close()
        f=open(os.path.join(os.getcwd()+"/Keys_IV",i),"wb")
        print(i)
        f.write(content)
        f.close()