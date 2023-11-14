from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_data(encrypted_data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data

def main():
    # Загружаем зашифрованные данные из файла
    with open("encrypted_file.bin", "rb") as file:
        encrypted_data = file.read()

    # Вводим ключ и вектор инициализации (IV)
    key = bytes.fromhex(input("Введите ключ в формате шестнадцатеричной строки (32 байта): "))
    iv = bytes.fromhex(input("Введите IV в формате шестнадцатеричной строки (16 байт): "))

    # Расшифровываем данные
    decrypted_data = decrypt_data(encrypted_data, key, iv)

    # Выводим расшифрованные данные
    print("Расшифрованные данные:", decrypted_data.decode('utf-8'))

if __name__ == "__main__":
    main()
