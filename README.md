# secure-qr-aes-sha256

This project aims to take a qr code image as imput, apply a series of operation and then deconstruct it into two encrypted images P and R. Upon applying the decryption algorithm, the orginal qr code image is regenerated. For encryption and decryption AES and SHA-256 algorithm have been applied. This repository contains Python scripts for image processing and cryptography tasks, demonstrating practical applications of these concepts in information security.

Image Encryption (encryption.py)

1. Encoding Image with Base64
The script reads an input image (qr_code_barcode.jpg) and encodes it using Base64 encoding.
The resulting Base64 encoded image data is stored in memory.
2. Generating Encryption Key
An encryption key is read from a text file (key.txt) and hashed using SHA-256 to generate a secure key.
3. AES-256 Encryption in OFB Mode
The AESCipher class implements AES-256 encryption in Output Feedback (OFB) mode.
The encoded image data is encrypted using the hashed key, and the result is Base64 encoded ciphertext.
4. Image Pixel Manipulation
A new image C is created based on the encrypted image data and the key.
Pixels are manipulated in C based on the key's characters, creating a unique pattern.
5. Saving Encrypted Images
The manipulated image C is saved as a PNG image (P.png) in the specified output directory.
Image Decryption (decryption.py)
1. Loading Encrypted Images
The script loads the encrypted images P.png and R.png generated by the encryption process.
2. XOR Operation to Reconstruct Image
The encrypted images P and R are XORed pixel by pixel to reconstruct the original encrypted image C.
3. Decrypting Text
The encrypted text is read from cipher2.txt, which was generated during encryption.
AES-256 decryption in OFB mode is performed using the previously hashed key to decrypt the text.
4. Regenerating QR Code
The decrypted text is converted back to binary and used to regenerate a QR code image.
The QR code is saved as regenerated_qr_code.png.
Dependencies
Python 3.x
OpenCV (cv2)
NumPy
Pillow (PIL)
pycryptodome
qrcode
pandas
scikit-learn
Usage
Install the required dependencies using pip install -r requirements.txt.
Run encryption.py to encrypt an image and generate encrypted images and text.
Run decryption.py to decrypt the encrypted images and text and regenerate the QR code.
