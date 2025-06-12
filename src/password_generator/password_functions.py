'''
Functions to generate random usernames and passwords.

'''
import secrets
import string

def generate_user_name(initials: str, n: int) -> str:

    return str(initials) + ''.join([secrets.choice(string.digits) for _ in range(n)])

def generate_password(n: int) -> str:

    return "".join([secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(n)])