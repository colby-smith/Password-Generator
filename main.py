import random
import string

    # make the user input there specified variables for the password
    # have the program define these variables and randomly generate a password from them
    # allow the user to accept this password as the one they'd like to use or let them keep generating till they're happy

def main():
    print ("--------------------------------Password Generator--------------------------------")
    define_password_length()
    print ("----------------------------------------------------------------------------------")
    define_special_characters()
    print ("----------------------------------------------------------------------------------")

def define_password_length():
    min_password_length = int(input("Please eneter the minimum amount of characters for your password, as a number: "))
    max_password_length = int(input("Please eneter the maximum amount of characters for your password, as a number: "))
    print ("----------------------------------------------------------------------------------")
    print (f"Your password will be generated between {min_password_length} and {max_password_length} characters.")
    if min_password_length > 50:
        raise Exception ("Minimum character length cannot be greater than 50")
    if min_password_length <= 0:
        raise Exception ("Minimum character length cannot be less than or equal to 0")
    if max_password_length > 50:
        raise Exception ("Maximum character length cannot be greater than 100")
    if max_password_length <= min_password_length:
        raise Exception ("Maximum password length cannot be less than minimum")
    else:
        return (min_password_length, max_password_length)
    
def define_special_characters():
    special_characters = (input("Would you like your password to contain special characters, yes or no: ")).lower()
    if special_characters == "yes":
        print ("----------------------------------------------------------------------------------")
        print ("Your password will contain special characters.")
        return (special_characters)
    else:
        print ("----------------------------------------------------------------------------------")
        print ("Your password will not contain special characters.")

main ()