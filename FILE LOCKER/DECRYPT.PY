from cryptography.fernet import Fernet, InvalidToken

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

with open("hello.txt", "rb") as file:
    data = file.read()

# Check if already decrypted
try:
    decrypted = fernet.decrypt(data)
    with open("hello.txt", "wb") as file:
        file.write(decrypted)
    print("🔓 File decrypted!")
except InvalidToken:
    print("⚠️ This file is already normal text. Nothing to decrypt.")