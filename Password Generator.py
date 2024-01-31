#-------------------------------------------------------------------------------
# Name:   TASK 3 = Password Generator


#-------------------------------------------------------------------------------

import random
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user's choice of complexity
    all_chars = lower_case + upper_case + digits + special_chars

    # Ensure the length is at least 8 characters
    length = max(8, length)

    # Generate the password using random.choices
    password = ''.join(random.choices(all_chars, k=length))

    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
