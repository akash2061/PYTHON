import itertools
import random
import string

def generate_passwords(size, uppercase, lowercase, numbers, special_chars):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    while True:
        password = ''.join(random.choice(characters) for _ in range(size))
        yield password

def write_passwords_to_file(filename, size, uppercase, lowercase, numbers, special_chars):
    with open(filename, 'w') as f:
        for password in generate_passwords(size, uppercase, lowercase, numbers, special_chars):
            f.write(password + '\n')

if __name__ == '__main__':
    filename = 'passwords.txt'

    size = int(input("Enter the size of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    write_passwords_to_file(filename, size, uppercase, lowercase, numbers, special_chars)
    print(f"Password list generated and saved to {filename}")

