from Encrypt import *
from Decrypt import *
from IVsKeys import *
import threading

def Crypt():
	iv1=generateIV()
	k1,k2=generateKey()
	CryptKeys()
	t1 = threading.Thread(target=AES, args=(k1,iv1,))
	t2 = threading.Thread(target=AES, args=(k1,iv1,))
	t3 = threading.Thread(target=AES, args=(k1,iv1,))
	t4 = threading.Thread(target=AES, args=(k1,iv1,))
	t5 = threading.Thread(target=AES, args=(k2,iv1,))

    #Starting the Encription Process	
	t1.start() 
	t2.start() 
	t3.start()
	t4.start()
	t5.start()

    #Thread Sync.
	t1.join() 
	t2.join() 
	t3.join()   
	t4.join()
	t5.join()


 
def DeCrypt():
	DeCryptKeys()
	iv=FetchIV()
	k1,k2=FetchKey()
	t1 = threading.Thread(target=DAES, args=(k1,iv[0],))
	t2 = threading.Thread(target=DAES, args=(k1,iv[0],))
	t3 = threading.Thread(target=DAES, args=(k1,iv[1],))
	t4 = threading.Thread(target=DAES, args=(k1,iv[1],))
	t5 = threading.Thread(target=DAES, args=(k2,iv[1],))

    #Starting the Encription Process
	t1.start() 
	t2.start() 
	t3.start()
	t4.start()
	t5.start()

    #Thread Sync.
	t1.join() 
	t2.join() 
	t3.join()
	t4.join()
	t5.join()