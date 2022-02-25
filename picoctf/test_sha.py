import hashlib
from cryptography.fernet import Fernet
import base64

username_trial = b"FRASER"
print(hashlib.sha256(username_trial).hexdigest()[4])