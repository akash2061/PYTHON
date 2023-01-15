import string
import random

length = int(input("Enter password length: "))

print('''Choose character set for password from these :
        1. Letters
        2. Digits
        3. Special characters
        4. Generate password''')

characterList = ""

while (True):
    choice = int(input("Pick a number "))
    if (choice == 1):

        characterList += string.ascii_letters
    elif (choice == 2):

        characterList += string.digits
    elif (choice == 3):

        characterList += string.punctuation
    elif (choice == 4):
        break
    elif (choice == 0):
        characterList += string.punctuation + string.digits + string.ascii_letters
        break

    else:
        print("Please pick a valid option!")

# if its good then ask 1 more time.

password = []

for i in range(length):

    randomchoice = random.choice(characterList)
    password.append(randomchoice)

print("The random password is " + "".join(password))