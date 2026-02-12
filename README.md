# Secure Login System (Python)

This project demonstrates an insecure login system to a more secure authentication model using password hashing and salting.

## Version 1 (Insecure)
- Stored plaintext passwords in memory
- Compared raw strings for authentication
- Limited login attempts
- Basic input validation

## Version 2 (Secure)
Improvements include:

### 🔐 Password Hashing
- Uses PBKDF2 with SHA-256
- 120,000 iterations
- Converts passwords into irreversible hashes

### 🧂 Salting
- Each user gets a unique 16-byte random salt
- Prevents identical passwords from producing identical hashes
- Protects against rainbow table attacks

### 🛡 Constant-Time Comparison
- Uses `hmac.compare_digest()`
- Reduces risk of timing-based attacks

### 🔄 Brute-Force Protection
- Limits login attempts to 3
- Locks system after repeated failures

### 🧹 Input Validation
- Username format restrictions
- Password length limits
- Empty input checks

## Security Concepts Demonstrated
- Password hashing vs plaintext storage
- Salted hashing
- Secure verification workflow
- Brute-force mitigation
- Authentication flow control

## How to Run
```bash
python secure_login.py
