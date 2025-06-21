# Gestione credenziali
import bcrypt
import json
import os

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# registra utente con una password protetta usando la libreria bcrypt
def register_user(username, password):
    users = load_users()
    if username in users:
        return False  # Utente già esistente
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())     # calcolo dell'hash sicuro della password, combinando password e salt
    users[username] = hashed.decode()                               # conversione byte in stringa: da b'$2b$12$abc...' a '$2b$12$abc...'
    save_users(users)
    return True

# verifica se username e password inseriti sono corretti usando la libreria bcrypt
def check_login(username, password):
    users = load_users()
    if username not in users:
        return False
    hashed = users[username].encode()                   # conversione della password fornita in byte
    return bcrypt.checkpw(password.encode(), hashed)    # conversione della password inserita con l’hash salvato
