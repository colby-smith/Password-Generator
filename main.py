import random
import string

    # make the user input there specified variables for the password
    # have the program define these variables and randomly generate a password from them
    # allow the user to accept this password as the one they'd like to use or let them keep generating till they're happy

def main():
    print ("------------------------Password Generator------------------------")
    define_password_length()

def define_password_length():
    min_password_length = int(input("Please eneter the minimum amount of characters for your password as numbers: "))
    max_password_length = int(input("Please eneter the maximum amount of characters for your password as numbers: "))
    if min_password_length > 50:
        raise Exception ("Minimum character length cannot be greater than 50")
    if min_password_length <= 0:
        raise Exception ("Minimum character length cannot be less than or equal to 0")
    if max_password_length > 50:
        raise Exception ("Maximum character length cannot be greater than 100")
    if max_password_length <= min_password_length:
        raise Exception ("Maximum password length cannot be less than minimum")
    else:
        print (min_password_length, max_password_length)

main ()