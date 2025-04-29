from cryptography.fernet import Fernet
import os
import json
from pathlib import Path

# Singleton cipher instance
_fernet = None

def get_cipher():
    global _fernet
    if _fernet is None:
        key_file = "secret.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
        _fernet = Fernet(key)
    return _fernet

DATA_FILE = "secure_data.json"

def save_to_json(data):
    """Encrypted data ko JSON mein save kare"""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)  # indent for readability
        return True
    except Exception as e:
        print(f"❌ Error saving JSON: {e}")
        return False

def load_from_json():
    """JSON se data load kare (App startup pe)"""
    try:
        if Path(DATA_FILE).exists():
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        return {}  # Empty dict if file doesn't exist
    except Exception as e:
        print(f"❌ Error loading JSON: {e}")
        return {}

# get_cipher()
