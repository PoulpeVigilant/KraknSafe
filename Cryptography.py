from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
print("---------------------------------------------")
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
print(cipher_text)
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text)