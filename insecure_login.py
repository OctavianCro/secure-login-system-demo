# insecure login version 1.0
users = {
    "tay": "password123",
    "gabriel": "hackthis123"
}

print("=== Insecure Login System ===")
attempts = 0
maxattempts = 3

def is_valid_username(username: str) -> bool:
    return username.isidentifier() and len(username) <= 15
def is_valid_password(password: str) -> bool:
    return 1 <= len(password) <= 20

while attempts < maxattempts:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if not username or not password:
            print ("Username and password cannot be empty.")
            continue
        
        if not is_valid_username(username):
            print("Username must be letters/numbers/underscore only (max 15).")
            continue
        
        if not is_valid_password(password):
            print("Password length must be 1–20 characters.")
            continue
    
        storedpasswords = users.get(username)
        
# INSECURE: passwords stored + compared in plain text"""
        if storedpasswords == password:
            print(f"Welcome, {username}")
            break
        else: 
            attempts += 1
            remaining = maxattempts - attempts
            print(f"Invlaid username or password. Try again. Attempts remaining: {remaining}")
    
if attempts == maxattempts:
    print("To many failed attempts, account is now locked..")
    
    
    
    
