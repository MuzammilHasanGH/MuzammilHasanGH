import random
import string

def generate_password(length, include_digits, include_symbols):
    characters = string.ascii_letters  # include both uppercase and lowercase letters
    
    if include_digits:
        characters += string.digits  # add digits if required
    
    if include_symbols:
        characters += string.punctuation  # add symbols if required
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get the password requirements from the user
    length = int(input("Enter the desired length of the password: "))
    include_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    # Generate the password
    password = generate_password(length, include_digits, include_symbols)
    
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
