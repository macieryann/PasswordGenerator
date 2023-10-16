import random
import string

# define function to generate password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# accept user input about pass length
def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length: "))
            return length
        except ValueError:
            print("Oops, please enter a valid number")

# main script execution
if __name__ == "__main__":
    length = get_password_length()
    password = generate_password(length)
    print("Your password is:", password)