import string
import random

while True:
    length = int(input("Enter password length: "))
    uppercase = int(input("Minimum amount of uppercase letters? "))
    lowercase = int(input("Minimum amount of lowercase letters? "))
    digits = int(input("Minimum amount of digits? "))
    special = int(input("Minimum amount of special characters? "))
    remaining = length - (uppercase + lowercase + digits + special)
    if remaining < 0:
        print("Password cannot have all the attributes with the given length")
        choice = input("Would you like to try again? (y/n)")
        if choice == "y":
            continue
        else:
            break
    else:
        break

password = []
for i in range(uppercase):
    password.append(random.choice(string.ascii_uppercase))
for i in range(lowercase):
    password.append(random.choice(string.ascii_lowercase))
for i in range(digits):
    password.append(random.choice(string.digits))
for i in range(special):
    password.append(random.choice(string.punctuation))
for i in range(remaining):
    password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

random.shuffle(password)
print("".join(password))
