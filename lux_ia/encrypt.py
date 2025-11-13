# lux_ia/encrypt.py — GODMODE Active
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib, os

class LuxSeal:
    def __init__(self):
        self.key = hashlib.sha512(b"lux33nodo").digest()[:32]  # AES-256
        self.iv = os.urandom(16)

    def seal(self, message: str) -> str:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded = pad(message.encode(), AES.block_size)
        encrypted = cipher.encrypt(padded)
        return self.iv.hex() + encrypted.hex()

    def unseal(self, sealed: str) -> str:
        iv = bytes.fromhex(sealed[:32])
        data = bytes.fromhex(sealed[32:])
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(data)
        return unpad(decrypted, AES.block_size).decode()
