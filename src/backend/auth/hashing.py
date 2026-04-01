from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def hash(input):
     return password_hash.hash(input)

def verify(input, hashed_input):
     return password_hash.verify(input, hashed_input)