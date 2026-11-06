import curses.ascii
import secrets
import string
import math

def generate_password(lenghth=12):
    """Generates a secure password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(lenghth))

    return password

def calculate_entropy(password):
    """Calculates entropy (bits of security) for a given password."""
    char_pool = 0
    if any(c.islower() for c in password):
        char_pool += 26
    if any(c.isupper() for c in password):
        char_pool += 26
    if any(c.isdigit() for c in password):
        char_pool += 10
    if any(c in string.punctuation for c in password):
        char_pool += len(string.punctuation)

    entropy = math.log2(char_pool ** len(password))

    return entropy

print(generate_password())