from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import secrets

# Генерируем случайный ключ и вектор инициализации (IV)
with open("key.file", 'r+') as key_file:

    key = key_file.readline()
    iv = key_file.readline()

# Функция для шифрования данных
def encrypt_data(data, key, iv):
    cipher = Cipher(algorithms.AES(bytes(str(key).encode())), modes.CFB(bytes(str(iv).encode())), backend=default_backend())
    print('key:', key, 'iv:', iv )
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    return encrypted_data

# Сохраняем зашифрованные данные в файл
data_to_encrypt = b"CTF{This_is_the_secret_flag}"
encrypted_data = encrypt_data(data_to_encrypt, key, iv)

with open("encrypted_file.bin", "wb") as file:
    file.write(encrypted_data)
