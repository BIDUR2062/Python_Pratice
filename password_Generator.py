import random as rd
import string

symbols = "!@#$%^&*"

password_length = int(input("Enter password length: "))

if password_length < 4:
    print("Password length must be at least 4.")
else:
    password = [
        rd.choice(string.ascii_lowercase),
        rd.choice(string.ascii_uppercase),
        rd.choice(string.digits),
        rd.choice(symbols)
    ]

    all_characters = string.ascii_letters + string.digits + symbols

    for _ in range(password_length - 4):
        password.append(rd.choice(all_characters))

    rd.shuffle(password)

    print("Generated Password:", "".join(password))