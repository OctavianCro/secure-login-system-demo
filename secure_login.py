#version 2: more secure (hashed passwords + verify safely)

import hashlib
import os
import hmac

print("=== Secure Login System ===")
attempts = 0
maxattempts = 3

def is_valid_username(username: str) -> bool:
    return username.isidentifier() and len(username) <= 15

def is_valid_password(password: str) -> bool:
    return 1 <= len(password) <= 20

def hash_password(password: str, salt: bytes) -> str:
    """ this will return a hex string hash using pbkdf2"""
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 120_000)
    return dk.hex()

#data base for the demo: store salt + password_hash (NOT the real password)
users = {}

def add_user(username: str, password: str) -> None:
    salt = os.urandom(16)
    password_hash = hash_password(password, salt)
    users[username] = {
        "salt": salt,
        "hash": password_hash
    }

add_user("tay", "password123")
add_user("gabriel", "hackthis123")

while attempts < maxattempts:
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if not username or not password:
        print("Username and password cannot be empty.")
        continue
    
    if not is_valid_username(username):
        print("Username must be letters/numbers/underscore only (max 15).")
        continue
    
    if not is_valid_password(password):
        print("Password length must be 1–20 characters.")
        continue
    
    record = users.get(username)

    if record is None:
        attempts += 1
        remaining = maxattempts - attempts
        print(f"Invalid username or password. Attempts remaining: {remaining}")
        continue

    salt = record["salt"]
    expected_hash = record["hash"]   
    candidate_hash = hash_password(password, salt)

    if hmac.compare_digest(candidate_hash, expected_hash):
        print(f"Welcome, {username}")
        break
    else:
        attempts += 1
        remaining = maxattempts - attempts
        print(f"Invalid username or password. Attempts remaining: {remaining}")

if attempts == maxattempts:
    print("Too many failed attempts, account is now locked")
