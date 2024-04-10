import base64
# Reading input Image and encoding it using base64
 
with open(r'/Users/priyanshusingh/Desktop/CRYPTO PROJ/content/qr_code_barcode.jpg', "rb") as img_file:
    BI = base64.b64encode(img_file.read())
print(BI)
BI = BI.decode("utf-8")
import hashlib
# My key
K = ""
f = open(r'/Users/priyanshusingh/Desktop/CRYPTO PROJ/content/key.txt','r')
 

for i in f:
    K += i
f.close()
K
SK = hashlib.sha256(K.encode())
 
print("The hexadecimal equivalent of SHA256 is : ")
print(SK.hexdigest())
# AES 256 in OFB mode:
from Crypto.Cipher import AES
from Crypto.Random import new as Random
from hashlib import sha256
from base64 import b64encode,b64decode
 
class AESCipher:
    def __init__(self,data,key):
        self.block_size = 16
        self.data = data
        self.key = sha256(key.encode()).digest()[:32]
        self.pad = lambda s: s + (self.block_size - len(s) % self.block_size) * chr (self.block_size - len(s) % self.block_size)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
    def encrypt(self):
        plain_text = self.pad(self.data)
        iv = Random().read(AES.block_size)
        cipher = AES.new(self.key,AES.MODE_OFB,iv)
        return b64encode(iv + cipher.encrypt(plain_text.encode())).decode()
    # Encrypting image using base 64 encoded text and hashed key - SHA256
# AES-256
c = AESCipher(BI,SK.hexdigest()).encrypt()
print(c)
import numpy as np
import cv2
w = 255
h = len(K)
# creating new Image C of size(w,h)
# initializing as blank
C = np.ones((h,w,1), dtype = 'uint8')
# Filling pixels in C
for i in range(h):
    j = ord(K[i])
    for k in range(w):
        if k < j:
            C[i][k][0] = 0
        else:
            break
 
# initializing R and P of same size as C
R = np.ones((h,w,3), dtype = 'uint8')
P = np.ones((h,w,3), dtype = 'uint8')
# filling the pixels of R
for i in range(h):
    for j in range(w):
        r = np.random.normal(0,1,1)
        R[i][j][0] = r
        # filling the pixels of P
for i in range(h):
    for j in range(w):
        p = R[i][j][0] ^ C[i][j][0]
        P[i][j][0] = p
f# Specify the output directory where R.png and P.png will be saved
output_dir = r'content'
 
# Save R.png and P.png images
import os
 
filename_R = os.path.join(output_dir, 'R.png')
filename_P = os.path.join(output_dir, 'P.png')
 
# Use cv2.imwrite() to save the images
cv2.imwrite(filename_R, R)
cv2.imwrite(filename_P, P)
 
# Print a message indicating successful image saving
print("Images R.png and P.png saved successfully.")
 
import pandas as pd
xdf = pd.DataFrame(columns = ['1','2'])
a = []
b = []
for i in P:
    k = 0
    n1 = []
    n2 = []
    for j in i:
        if k%2==0:
            n1.append(np.sum(j))
        else:
            n2.append(np.sum(j))
        k += 1
    a.append(sum(n1))
    b.append(sum(n2))
xdf['1'] = a
xdf['2'] = b
ydf = pd.DataFrame(columns = ['1','2'])
a = []
b = []
for i in R:
    k = 0
    n1 = []
    n2 = []
    for j in i:
        if k%2==0:
            n1.append(np.sum(j))
        else:
            n2.append(np.sum(j))
        k += 1
    a.append(sum(n1))
    b.append(sum(n2))
ydf['1'] = a
ydf['2'] = b
from sklearn.linear_model import LinearRegression
LRmodel = LinearRegression()
LRmodel.fit(xdf,ydf)
# z is for prediction
zdf = pd.DataFrame(columns = ['1','2'])
a = []
b = []
for i in C:
    k = 0
    n1 = []
    n2 = []
    for j in i:
        if k%2==0:
            n1.append(np.sum(j))
        else:
            n2.append(np.sum(j))
        k += 1
    a.append(sum(n1))
    b.append(sum(n2))
zdf['1'] = a
zdf['2'] = b
predict = LRmodel.predict([[sum(zdf['1']),sum(zdf['2'])]])
x = round(predict[0][0])%26
y = round(predict[0][1])%26
txt = []
for each in c:
    ch = ord(each) + x - y
    txt.append(int(ch))
text = ""
for t in txt:
    text += chr(t) + " "
    f = open(r"content/cipher2.txt", 'a', encoding='utf-8')
 
f.write(text)
f.close()
