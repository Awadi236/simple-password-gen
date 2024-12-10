import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Random Password Generator")
    try:
        length = int(input("Enter password length: "))
        print(f"Generated Password: {generate_password(length)}")
    except ValueError:
        print("Invalid input! Please enter a number.")
