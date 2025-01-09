import sqlite3
from cryptography.fernet import Fernet
import os
import secrets
import string
from tkinter import Tk, Label, Entry, Button, Text, END

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

# Functions for password manager
def add_password(account, password):
    encrypted_password = cipher.encrypt(password.encode())
    cursor.execute("INSERT INTO passwords (account, password) VALUES (?, ?)", (account, encrypted_password))
    conn.commit()
    output_box.insert(END, "Password saved successfully.\n")

def retrieve_password(account):
    cursor.execute("SELECT password FROM passwords WHERE account = ?", (account,))
    result = cursor.fetchone()
    if result:
        decrypted_password = cipher.decrypt(result[0]).decode()
        output_box.insert(END, f"Password for {account}: {decrypted_password}\n")
    else:
        output_box.insert(END, "Account not found.\n")

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def handle_add_password():
    account = account_entry.get()
    password = password_entry.get()
    if account and password:
        add_password(account, password)
    else:
        output_box.insert(END, "Please enter both account and password.\n")

def handle_retrieve_password():
    account = account_entry.get()
    if account:
        retrieve_password(account)
    else:
        output_box.insert(END, "Please enter the account name.\n")

def handle_generate_password():
    length = 12  # Default length
    generated_password = generate_password(length)
    output_box.insert(END, f"Generated password: {generated_password}\n")

# GUI Setup
root = Tk()
root.title("Password Manager")

# Labels and Inputs
Label(root, text="Account:").grid(row=0, column=0, padx=10, pady=5)
account_entry = Entry(root)
account_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = Entry(root)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons
Button(root, text="Add Password", command=handle_add_password).grid(row=2, column=0, padx=10, pady=10)
Button(root, text="Retrieve Password", command=handle_retrieve_password).grid(row=2, column=1, padx=10, pady=10)
Button(root, text="Generate Password", command=handle_generate_password).grid(row=3, column=0, columnspan=2, pady=10)

# Output Box
output_box = Text(root, height=10, width=50)
output_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI
root.mainloop()

