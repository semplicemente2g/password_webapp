import json
import bcrypt

USER_DB = 'users.json'

# Lista di password comuni
dictionary = [
    'password',
    '123456',
    '000000',
    'juventus',
    'abc123',
    'spiderman',
    'batman',
    'Bologna',
    'mariorossi'
]

def load_users():
    with open(USER_DB, 'r') as f:
        return json.load(f)

def dictionary_attack():
    users = load_users()
    found = {}
    for username, hashed_pw in users.items():
        for pwd in dictionary:
            # bcrypt usa hashed_pw in byte
            if bcrypt.checkpw(pwd.encode('utf-8'), hashed_pw.encode('utf-8')):
                found[username] = pwd
                break
    return found

if __name__ == '__main__':
    compromised = dictionary_attack()
    if compromised:
        print("Password trovate con l'attacco dizionario:")
        for user, pwd in compromised.items():
            print(f"- Utente: {user} | Password: {pwd}")
    else:
        print("Nessuna password trovata con il dizionario.")
