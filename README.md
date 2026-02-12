# secure login system (python)

This project demonstrates an insecure login system to a more secure authentication model using password hashing and salting.

## version 1 (insecure)
- only stored plaintext passwords in memory
- compared raw strings for authentication
- limited login attempts
- basic input validation

## version 2 (secure)
improvements include:

### password hashing
- uses PBKDF2 with SHA-256
- 120,000 iterations
- converts passwords into irreversible hashes

### salting
- each user will get a unique 16-byte random salt
- prevents identical passwords from producing identical hashes
- protects against rainbow table attacks

### constant time comparison
- uses `hmac.compare_digest()`
- it reduces risk of timing-based attacks

### brute force protection
- limits login attempts to 3
- locks system after repeated failures

### input validation
- username format restrictions
- password length limits
- empty input checks

## security concepts
- password hashing vs plaintext storage
- salted hashing
- secure verification workflow
- brute force mitigation
- authentication flow control

## how to run
```bash
python secure_login.py
