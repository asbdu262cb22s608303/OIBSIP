# Random Password Generator - Oasis Infobyte Task 3
# Developed by Shafika Mariyam B

import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main Program
print("=== Random Password Generator ===")
print("Developed by Shafika Mariyam B - OIBSIP Task 3")

try:
    length = int(input("Enter password length (e.g., 8, 12, 16): "))
    
    print("\nCustomize your password:")
    letters = input("Include letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    password = generate_password(length, letters, numbers, symbols)
    
    print(f"\nYour Generated Password is: {password}")
    print("\nKeep it safe and secure!")
    
except ValueError:
    print("Please enter a valid number for length!")
