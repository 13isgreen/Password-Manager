Python Password Manager

Overview
The Python Password Manager is a lightweight and secure tool for storing, managing, and generating passwords.
It ensures the confidentiality of stored credentials by encrypting them using advanced cryptographic techniques.

Features
Secure Storage: Passwords are encrypted using the AES encryption algorithm (via the Fernet module) before being stored in an SQLite database.

Password Retrieval: Retrieve your saved passwords securely by searching for the associated account name.

Random Password Generator: Generate strong, random passwords with customizable length, including a mix of letters, numbers, and symbols.

Ease of Use: User-friendly command-line interface for adding, retrieving, and generating passwords.
Technologies Used

Programming Language: Python

Database: SQLite

Encryption Library: PyCryptodome (Fernet module)

How It Works
The program generates a unique encryption key (saved locally in key.key) to encrypt and decrypt passwords.
Passwords and account names are stored in a local SQLite database after encryption.
Users can interact with the program through a menu-based CLI to:
Add new account-password pairs.
Retrieve passwords for specific accounts.
Generate and copy strong passwords.

Setup and Installation
Clone this repository to your local machine:
git clone <repository_url>
Install the required Python libraries:
pip install cryptography
Run the program:
python password_manager.py

Posisble issues:
If your using a version of python before 3.6, you'll have to install the gui dependiencies
(Debian)
sudo apt-get install python3-tk
(Fedora)
sudo dnf install python3-tkinter

You can check to ensure the dependiecis are properly installed with 
python -m tkinter

Future Enhancements
Add a master password for securing the tool.
Integrate a graphical user interface (GUI).
Add features like password strength evaluation and export/import functionality.
Disclaimer
This tool is for personal use and learning purposes only. Ensure the security of your local environment to protect sensitive data stored by the password manager.
