from cryptography.fernet import Fernet, InvalidToken

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

with open("hello.txt", "rb") as file:
    data = file.read()

# Check if already encrypted
try:
    fernet.decrypt(data)
    print("⚠️ File is already decrypted. Encrypting now...")
except InvalidToken:
    print("🔒 File is already encrypted.")

# Encrypt only if it is not encrypted
if not data.startswith(b"gAAAA"):
    encrypted = fernet.encrypt(data)
    with open("hello.txt", "wb") as file:
        file.write(encrypted)
    print("🔒 File encrypted!")
else:
    print("⚠️ Not encrypting again.")