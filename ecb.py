
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# Clave de 16 bytes (AES-128)
key = os.urandom(16)

# Crear un cifrador en modo ECB
cipher = Cipher(algorithms.AES(key), modes.ECB())

# Leer la imagen BMP de entrada
with open('1.bmp', 'rb') as f:
    img_data = f.read()

# Leer la cabecera de la imagen (primeros 54 bytes)
img_header = img_data[:54]

# Cuerpo de la imagen (sin la cabecera)
img_body = img_data[54:]

# Agregar relleno PKCS7 al cuerpo de la imagen
padder = padding.PKCS7(128).padder()
padded_img_body = padder.update(img_body) + padder.finalize()

# Cifrar el cuerpo de la imagen
encryptor = cipher.encryptor()
ciphertext_body = encryptor.update(padded_img_body) + encryptor.finalize()

# Combinar la cabecera de la imagen y el cuerpo cifrado
ciphertext_img = img_header + ciphertext_body

# Guardar la imagen cifrada en un nuevo archivo
with open('encrypted.bmp', 'wb') as f:
    f.write(ciphertext_img)

# Descifrar la imagen
decryptor = cipher.decryptor()

# Separar la cabecera y el cuerpo cifrado de la imagen cifrada
decrypted_img_header = ciphertext_img[:54]
ciphertext_body = ciphertext_img[54:]

# Descifrar el cuerpo cifrado de la imagen
decrypted_padded_img_body = decryptor.update(ciphertext_body) + decryptor.finalize()

# Eliminar el relleno PKCS7 del cuerpo descifrado
unpadder = padding.PKCS7(128).unpadder()
decrypted_img_body = unpadder.update(decrypted_padded_img_body) + unpadder.finalize()

# Combinar la cabecera y el cuerpo descifrado
decrypted_img = decrypted_img_header + decrypted_img_body

# Guardar la imagen descifrada en un nuevo archivo
with open('decrypted.bmp', 'wb') as f:
    f.write(decrypted_img)

print("Imagen cifrada y descifrada exitosamente.")

