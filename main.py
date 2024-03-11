import random
import string
import time

PASSWORD_LETTERS = string.ascii_letters
PASSWORD_DIGITS = string.digits
PASSWORD_SPECIAL = string.punctuation
    # make the user input there specified variables for the password
    # have the program define these variables and randomly generate a password from them
    # allow the user to accept this password as the one they'd like to use or let them keep generating till they're happy

def main():
    print ("--------------------------------Password Generator--------------------------------")
    min_password_length, max_password_length = define_password_length()
    print ("----------------------------------------------------------------------------------")     
    contains_special_characters = define_special_characters()
    print ("----------------------------------------------------------------------------------")
    contains_digits = define_digits()
    print ("----------------------------------------------------------------------------------")
    length = random.randint(min_password_length, max_password_length)
    
    if contains_special_characters and contains_digits:
        population = PASSWORD_LETTERS + PASSWORD_DIGITS + PASSWORD_SPECIAL
    elif contains_special_characters:
        population = PASSWORD_LETTERS + PASSWORD_SPECIAL
    elif contains_digits:
        population = PASSWORD_LETTERS + PASSWORD_DIGITS
    else:
        population = PASSWORD_LETTERS

    print(''.join(random.choice(population) for _ in range(length)))
    

def define_password_length():
    min_password_length = int(input("Please eneter the minimum amount of characters for your password, as a number: "))
    max_password_length = int(input("Please eneter the maximum amount of characters for your password, as a number: "))
    print ("----------------------------------------------------------------------------------")
    print (f"Your password will be generated between {min_password_length} and {max_password_length} characters.")
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
        print ("Your password will contain special characters.")
        return True
    else:
        print ("----------------------------------------------------------------------------------")
        print ("Your password will not contain special characters.")
        return False

def define_digits():
    contains_digits = (input("Would you like your password to contain digits, yes or no: ")).lower()
    if contains_digits == "yes":
        print ("----------------------------------------------------------------------------------")
        print ("Your password will contain digits.")
        return True
    else:
        print ("----------------------------------------------------------------------------------")
        print ("Your password will not contain digits.")
        return False

main ()