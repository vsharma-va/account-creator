from userClass import User
import string
import random


def openFile():
    with open("L:\\Python Projects\\Updated Bank Program\\bankaccount\\bankaccount\\registeredPins.txt", 'r') as file:
        pins = file.readlines()
    file.close()
    return pins


def writeFile(data):
    with open("L:\\Python Projects\\Updated Bank Program\\bankaccount\\bankaccount\\registeredPins.txt", 'r+') as file:
        file.write(data)
    file.close()


def removePunctuation(pins):
    punctuationMarks = string.punctuation
    for i in pins:
        if i == punctuationMarks:
            pins.remove(i)
    return pins


def removeSpaces(pins):
    cleanListPins = []
    for z in pins:
        cleanListPins.append(z.strip())
    return cleanListPins


def cleanListofPins():
    cleanList = removeSpaces(removePunctuation(openFile()))
    return cleanList


def greetUser():
    registeredPins = cleanListofPins()
    userInDataBase: bool = True
    lenRegisteredPins = len(registeredPins)
    elementIndex = 0
    chances = 3
    print("Welcome to Axis Bank\n")

    try:
        registered = int(input('''Are you registered with us?
press 1 for yes
press 2 for no\n'''))
    except TypeError:
        print("Entered a string")
    if registered == 1:
        for i in range(chances):    
            userName = input("Enter your registered name: ")
            userPin = input("Enter your registered Pin: ")
            for z in registeredPins:
                search = userName + ' ' + userPin
                if search == z:
                    print("Welcome")
                    userInDataBase = True
                    break
                elif search != z and elementIndex != lenRegisteredPins - 1:
                    elementIndex += 1
                    userInDataBase = False
                elif elementIndex == lenRegisteredPins - 1:
                    print("Your input doesn't match with our records " +
                    " Either you are not registered with us or you have " +
                    " Entered the wrong information " + " Please try again ")
                    elementIndex = 0
                    chances += 1
    elif registered == 2:
        print("would you like to register?")
        userInDataBase = False
    return userInDataBase


def inputChecker(data: str, length, strict= 0):
    if len(data) >= length and not strict == 1:
        return True
    elif strict == 1:
        if len(data) == length:
            return True
        elif len(data) >= length:
            return False
    else:
        return False


def registerAccount():
    registeredPins = cleanListofPins()
    correct: bool = False
    enterNameAgain: bool = False
    numberOfTries: int = 0 
    try:
        wantsAccount = int(input("Press 1 to register a account "+"\nPress 2 to exit \n"))  # asks user if he/she wants to register an account
    except TypeError:
        print("You entered a string")  # checks the value of wantsAccount
    if wantsAccount == 1:
        while not correct:
            if enterNameAgain or numberOfTries == 0:
                firstName = input("Enter your first name: ")
                lastName = input("Enter your last name: ")
                pin = input("Enter your desired Pin (Must be 4 integers): ")
            else:
                pin = input("Enter your desired Pin (Must be 4 integers): ")

            if inputChecker(firstName, 2) and inputChecker(lastName, 2) and inputChecker(pin, 4, 1):

                rePin = input("Enter your pin again for conformation: ")
                if rePin == pin:
                    correct = True
                    newUser = User(firstName, lastName, pin)  # fills the input to the User class in the file userClass.py in the same directory
                    newUser.describeUser()
                    userData = firstName + ' ' + pin
                    registeredPins.append(userData)
                    writeFile(userData)
                    break
                elif rePin != pin:
                    print("The two pins don't match\n")
                    enterNameAgain = False
                    numberOfTries += 1

            else:
                print("Please input correct Info")
                correct = False
                enterNameAgain = True
                numberOfTries += 1
                continue
    return correct


def accountNumberGenerator():
    accountLength = 10
    # random account generator which cannot have 0 as the first digit
    newAccountNumber = ""
    for i in range(0, accountLength, 1):
        if i == 0:
            digit = str(random.randint(1, 9))
            newAccountNumber += digit
        else:
            digit = str(random.randint(0, 9))
            newAccountNumber += digit
    return int(newAccountNumber)


def newAccountDeposit():
    correctDeposit: bool = False
    while not correctDeposit:
        moneyDeposit = float(input())
        if moneyDeposit < 1000:
            print("Minimum deposit is 1000")
        else:
            balance = moneyDeposit
            correctDeposit = True
            break


def main():
    exit: bool = False
    registeredUser: bool = greetUser()
    while not exit:
        if not registeredUser:
            if registerAccount():
                print("your new account number is:", accountNumberGenerator(), "\nDo not share this number with anyone!")
                print("Your minimum deposit will be $1000")
                print("Enter amount to deposit: ")
                newAccountDeposit()
                break
            else:
                print("Have a good day")
                exit = True
                break
        elif registeredUser:
            print("Good day")
            exit = True
            break


main()
