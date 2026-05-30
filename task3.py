# secure_login.py

import hashlib

stored_username = "admin"

# Hash of "admin123"
stored_password_hash = hashlib.sha256(
    "admin123".encode()
).hexdigest()

attempts = 3

while attempts > 0:

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    if username == stored_username and password_hash == stored_password_hash:
        print("Login Successful")
        break

    attempts -= 1
    print(f"Invalid Credentials. Attempts Left: {attempts}")

if attempts == 0:
    print("Account Locked!")