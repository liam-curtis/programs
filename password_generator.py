import random
import string

"""
Name of program: password generator

Purpose: create a random password for the user, and output the random password to the user.
Password should have at least one upper case letter, one lower case letter, and one number, 
and be 8 characters long.

Date: 12/16/22

"""
def main():
    
    username = input("Hello!\nEnter username:")
    password = createPassword(int(input("Hi " + username +"!\nHow long would you like your random password to be? (please enter a positive integer): ")))
    print("Sounds good, Your username and password are all set!\nUsername: " + username + "\nPassword: " + password)

def createPassword(length):
    #combines the other functions to create the password
    word = (characters(length))
    word = passwordMixer(word)
    word = concatenateList(word)
    return word
    
def characters(length):
    
    #initializes the spread of characters a password will have (upper, lower, num)
    numLower = random.randint(1,length-2)
    numUpper = random.randint(1,length-numLower-1)
    numNum = length - (numUpper+numLower)
    
    #initializes, creates, and returns an unscrambled password in array form
    character = []
    for x in range(numLower):
        character.append(random.choice(string.ascii_lowercase))
    for x in range(numUpper):
        character.append(random.choice(string.ascii_uppercase))
    for x in range(numNum):
        character.append(random.choice(string.digits))
        
    return character
    
def passwordMixer(orig):
    # Scrambles the ordered list into a fully random one
    random.shuffle(orig)
    return orig

def concatenateList(arr):
    #concatenates the password into a string
    password = ""
    
    for x in range(len(arr)):
        password += arr[x]
        
    return password
    
if __name__ == "__main__": 
    main()
