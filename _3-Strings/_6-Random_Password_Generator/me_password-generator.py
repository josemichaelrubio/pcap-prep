import random
import string

def main():
    interact_main_menu()

def interact_main_menu():
    while True:
        print('\n-- Password generator --')
        print('Choose option:')
        print('1: generate password')
        print('2: exit the program')
        user_choice = input('Your choice: ')
        if user_choice == '1':
            length = int(input('Provide password length: '))
            include_upper = input('Use uppercase letters? (y/n): ').lower().strip() == 'y'
            include_digits = input('Use digits? (y/n): ').lower().strip() == 'y'
            include_special = input('Use special characters? (y/n): ').lower().strip() == 'y'
            print('\nGenerated password:', generate_password(length, include_upper, include_digits, include_special), '\n')
            break
        elif user_choice == '2':
            print('Bye!')
            break
        else:
            print('Please enter a correct value')
            interact_main_menu()

def generate_password(length, include_upper, include_digits, include_special):
    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

main();