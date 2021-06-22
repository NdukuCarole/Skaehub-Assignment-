import random
import string
import sys

# This function uses the string module to make random letters and numbers
def mixlist():
    return "".join(random.choice(string.ascii_letters + string.digits) for x in range(8))

# This function creates a random list of special characters
def special_list():
    return "".join(random.choice("?!&$*%@") for x in range(2))


def main():

    specials = special_list()
    mixed = mixlist()

    password = (mixed + specials)
    passwordlist = []
    passwordlist[:0] = password

#user input on choice of strength of password
    difficulty = str(input("Would you like your password to be weak or strong?"))

#password length for weak is 4 characters
    if difficulty.lower() == "weak":
        shufflelist = random.sample(passwordlist, len(passwordlist[0:4]))
        userpassword = "".join(shufflelist)
        print (userpassword)

        #ask user whether they are happy with the password
        happy = str(input("Are you happy with this password?  Y/N?"))
        if happy.upper() == "Y":
            sys.exit()
        elif happy.upper() == "N":
            main()

    elif difficulty.lower() == "strong":
        shufflelist = random.sample(passwordlist, len(passwordlist))
        userpassword = "".join(shufflelist)
        print(userpassword)
        happy = str(input("Are you happy with this password?  Y/N?"))
        if happy.upper() == "Y":
            sys.exit()
        elif happy.upper() == "N":
            main()
            
#incase of failure
    else:
        print ("Please try again, restarting generator")
        main()

main()