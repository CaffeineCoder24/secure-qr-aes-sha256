import cv2
import numpy as np

# Load P.png and R.png images
P = cv2.imread('/Users/priyanshusingh/Desktop/CRYPTO PROJ/content/P.png', cv2.IMREAD_COLOR)
R = cv2.imread('/Users/priyanshusingh/Desktop/CRYPTO PROJ/content/R.png', cv2.IMREAD_COLOR)

# Get image dimensions
height, width, _ = P.shape

# Reconstruct C by XORing P and R
C = np.zeros((height, width, 1), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        C[i][j][0] = P[i][j][0] ^ R[i][j][0]

# Read the key from key.txt
with open('/Users/priyanshusingh/Desktop/CRYPTO PROJ/content/key.txt', 'r') as f:
    key = f.read().strip()

# Decode the encrypted text from cipher2.txt
with open('/Users/priyanshusingh/Desktop/CRYPTO PROJ/content/cipher2.txt', 'r', encoding='utf-8') as f:
    encrypted_text = f.read()

# Decrypt the text using AES-256 in OFB mode
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64decode

# Define AES decryption function
def aes_decrypt(encrypted_data, key):
    cipher = AES.new(hashlib.sha256(key.encode()).digest()[:32], AES.MODE_OFB)
    encrypted_data = b64decode(encrypted_data)
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher.iv = iv
    try:
        decrypted_text = cipher.decrypt(ciphertext).decode('utf-8').strip()
    except UnicodeDecodeError:
        # Handle decoding error by replacing invalid bytes
        decrypted_text = cipher.decrypt(ciphertext).decode('utf-8', errors='replace')
    return decrypted_text

# Decrypt the encrypted text
decrypted_text = aes_decrypt(encrypted_text, key)

# Convert the decrypted text back to binary
binary_data = bytearray(decrypted_text.replace(" ", ""), encoding='utf-8')

# Regenerate the QR code
import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the binary data to the QR code
qr.add_data(binary_data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("/Users/priyanshusingh/Desktop/CRYPTO PROJ/content/regenerated_qr_code.png")