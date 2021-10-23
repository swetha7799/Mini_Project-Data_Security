from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

import os

def cn():
    i=0
    n=str(i+1)+".txt"
    return n
    
def AES(key,iv):
    n=cn()
    f=open(os.path.join(os.getcwd()+"/Parts",n),"r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%16!=0):
        while(b%16!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"/Parts",n),"wb").close()
    f=open(os.path.join(os.getcwd()+"/Parts",n),"wb")
    f.write(cont)
    f.close();


def CryptKeys():
    key = Fernet.generate_key()
    f=open('Secured.txt','wb')
    f.write(key)
    f.close()
    listDir=os.listdir(os.getcwd()+"/Keys_IV")
    fer = Fernet(key)
    for i in listDir:
        KI=open(os.getcwd()+'/Keys_IV//'+i,'rb')
        content=KI.read()
        KI.close()
        content=fer.encrypt(content)
        open(os.path.join(os.getcwd()+"/Keys_IV",i),'wb').close()
        f=open(os.path.join(os.getcwd()+"/Keys_IV",i),"wb")
        f.write(content)
        f.close()