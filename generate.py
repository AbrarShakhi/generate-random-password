import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

def randomly(length):
    password = ""
    for i in range(length):
        password += random.choice(chars)

    while not (any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()" for c in password)):
        index = random.randint(0, length - 1)
        password = password[:index] + \
            random.choice(chars) + password[index + 1:]

    return password