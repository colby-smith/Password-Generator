import random
import string
import time

PASSWORD_LETTERS = string.ascii_letters
PASSWORD_DIGITS = string.digits
PASSWORD_SPECIAL = string.punctuation

def main():
    print ("--------------------------------Password Generator--------------------------------")
    while True:
        password = generate_password()
        print("Your generated password:", password)
        print ("----------------------------------------------------------------------------------")
        response = input("Are you satisfied with this password? (yes/no): ").strip().lower()
        if response == "yes":
            print("Great! Your password has been generated above.")
            break
        elif response == "no":
            print("Generating a new password...")
            continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def generate_password():
    min_password_length, max_password_length = define_password_length()
    contains_special_characters = define_special_characters()
    contains_digits = define_digits()
    length = random.randint(min_password_length, max_password_length)

    if contains_special_characters and contains_digits:
        population = PASSWORD_LETTERS + PASSWORD_DIGITS + PASSWORD_SPECIAL
    elif contains_special_characters:
        population = PASSWORD_LETTERS + PASSWORD_SPECIAL
    elif contains_digits:
        population = PASSWORD_LETTERS + PASSWORD_DIGITS
    else:
        population = PASSWORD_LETTERS

    return ''.join(random.choice(population) for _ in range(length))
    
def define_password_length():
    min_password_length = int(input("Please eneter the minimum amount of characters for your password, as a number: "))
    max_password_length = int(input("Please eneter the maximum amount of characters for your password, as a number: "))
    print ("----------------------------------------------------------------------------------")
    if min_password_length > 50:
        raise Exception ("Minimum character length cannot be greater than 50")
    elif min_password_length <= 0:
        raise Exception ("Minimum character length cannot be less than or equal to 0")
    elif max_password_length > 50:
        raise Exception ("Maximum character length cannot be greater than 100")
    if max_password_length <= min_password_length:
        raise Exception ("Maximum password length cannot be less than minimum")
    else:
        return (min_password_length, max_password_length)
    
def define_special_characters():
    contains_special_characters = (input("Would you like your password to contain special characters, yes or no: ")).lower()
    if contains_special_characters == "yes":
        print ("----------------------------------------------------------------------------------")
        return True
    else:
        print ("----------------------------------------------------------------------------------")
        return False

def define_digits():
    contains_digits = (input("Would you like your password to contain digits, yes or no: ")).lower()
    if contains_digits == "yes":
        print ("----------------------------------------------------------------------------------")
        return True
    else:
        print ("----------------------------------------------------------------------------------")
        return False

main ()