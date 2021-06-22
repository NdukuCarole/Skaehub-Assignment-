#defining function
def lword(s):

    #use the method to split the words
        words = s.split()
        if len(words) == 0:
            return 0
#checks the word for the last 
        return len(words[-1])

        #user input 
cat=lword(input("please enter word "))

#Output expected
print(cat)
