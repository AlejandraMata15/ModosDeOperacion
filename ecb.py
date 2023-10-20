from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Función para cifrar una imagen BMP
def encrypt_image(input_file, output_file, key_file):
    # Leer la clave desde el archivo
    with open(key_file, 'rb') as f:
        key = f.read()

    # Leer la imagen BMP de entrada
    with open(input_file, 'rb') as f:
        img_data = f.read()

    # Extraer la cabecera de la imagen BMP (primeros 54 bytes)
    img_header = img_data[:54]

    # Cuerpo de la imagen (sin la cabecera)
    img_body = img_data[54:]

    # Inicialización del vector (IV) para el modo CBC
    iv = get_random_bytes(16)

    # Crear un cifrador en modo CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Cifrar el cuerpo de la imagen con relleno PKCS7
    ciphertext_body = cipher.encrypt(pad(img_body, AES.block_size))

    # Combinar la cabecera y el cuerpo cifrado
    ciphertext_img = img_header + ciphertext_body

    # Guardar la imagen cifrada en un nuevo archivo
    with open(output_file, 'wb') as f:
        f.write(ciphertext_img)

    print("Imagen cifrada exitosamente.")

# Función para descifrar una imagen BMP
def decrypt_image(input_file, output_file, key_file):
    # Leer la clave desde el archivo
    with open(key_file, 'rb') as f:
        key = f.read()

    # Leer la imagen cifrada
    with open(input_file, 'rb') as f:
        ciphertext_img = f.read()

    # Separar la cabecera y el cuerpo cifrado de la imagen cifrada
    img_header = ciphertext_img[:54]
    ciphertext_body = ciphertext_img[54:]

    # Inicialización del vector (IV) para el modo CBC
    iv = get_random_bytes(16)

    # Crear un cifrador en modo CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Descifrar el cuerpo cifrado de la imagen y eliminar el relleno PKCS7
    img_body = unpad(cipher.decrypt(ciphertext_body), AES.block_size)

    # Combinar la cabecera y el cuerpo descifrado
    decrypted_img = img_header + img_body

    # Guardar la imagen descifrada en un nuevo archivo
    with open(output_file, 'wb') as f:
        f.write(decrypted_img)

    print("Imagen descifrada exitosamente.")

# Ejemplo de uso:
# encrypt_image('input.bmp', 'encrypted.bmp', 'key.bin')
# decrypt_image('encrypted.bmp', 'decrypted.bmp', 'key.bin')

