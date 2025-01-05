import sqlite3
from cryptography.fernet import Fernet
import os
import secrets
import string

# Generate a key and save it if it doesn't exist
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("key.key", "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

# Connect to the SQLite database
conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

# Create table for storing passwords
cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY,
    account TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

def add_password(account, password):
    encrypted_password = cipher.encrypt(password.encode())
    cursor.execute("INSERT INTO passwords (account, password) VALUES (?, ?)", (account, encrypted_password))
    conn.commit()
    print("Password saved successfully.")

def retrieve_password(account):
    cursor.execute("SELECT password FROM passwords WHERE account = ?", (account,))
    result = cursor.fetchone()
    if result:
        decrypted_password = cipher.decrypt(result[0]).decode()
        print(f"Password for {account}: {decrypted_password}")
    else:
        print("Account not found.")

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Generate a random password")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            account = input("Enter the account name: ")
            password = input("Enter the password: ")
            add_password(account, password)
        elif choice == '2':
            account = input("Enter the account name: ")
            retrieve_password(account)
        elif choice == '3':
            length = int(input("Enter the desired password length: "))
            print(f"Generated password: {generate_password(length)}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
