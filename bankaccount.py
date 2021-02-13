from userClass import User
import random

registeredPins = [1234,3456,4567,5678,6789,7890]
def greetUser():
    userInDataBase: bool = True
    print("Welcome to Axis Bank\n")
    lenRegisteredPins = len(registeredPins)
    pinNumber = int(input("please Enter your account Number: "))
    for i in range(lenRegisteredPins - 1):
        if registeredPins[i] == pinNumber: #Checks the input account number with registered accounts from the list
            userInDataBase = True
            break
        if registeredPins[i] != pinNumber: #if no account number matches then the program asks the user to register
            userInDataBase = False
        
    if userInDataBase:
        print("Good day")
    else:
        print("You are not a registered user")
    return userInDataBase # returns bool value true if account number is in database else returns false


def registerAccount():
    try:
        wantsAccount = int(input("Press 1 to register a account "+"\nPress 2 to exit \n"))   #asks user if he/she wants to register an account
    except TypeError:
        print("You entered a string")                                                        #checks the value of wantsAccount
    if wantsAccount == 1:
        firstName = input("Enter your first name: ")
        lastName = input("Enter your last name: ")
        correct:bool = False
        while not correct:                                                                   #till correct is false it will keep asking the user to enter the password again
            numberOfLetterChecker = 0                                                        #checks if the length of password is greater than 4
            pin = (input("Enter your desired pin: "))
            while len(pin) != 4:
                print("your pin has to be 4 digits long")
                pin = (input("Enter your desired Pin: "))


            rePin = input("Please enter your pin again: ")                                   #asks user to confirm their pin
            if not rePin == pin:                                                             #checks if the confirm pin is equal to their oin
                 print("the two passwords dont match")
            elif rePin == pin:
                 correct = True
                 registeredPins.append(pin)                                                  #if they both are equal then the pin is added to the registeredPins list
        newUser = User(firstName, lastName, pin)                                             #fills the input to the User class in the file userClass.py in the same directory
        newUser.describeUser()
    else:
        pass
    return wantsAccount


def accountNumberGenerator():
    accountLength = 10
    newAccountNumber = ""                                           # random account generator which cannot have 0 as the first digit
    for i in range(0, accountLength, 1):
        if i == 0:
            digit = str(random.randint(1,9))
            newAccountNumber += digit
        else:
            digit = str(random.randint(0,9))
            newAccountNumber += digit
    return int(newAccountNumber)


def newAccountDeposit():
    correctDeposit:bool = False
    while not correctDeposit:
        moneyDeposit = float(input())
        if moneyDeposit < 1000:
            print("Minimum deposit is 1000")
        else:
            balance = moneyDeposit
            correctDeposit = True
            break


def main():
    exit:bool = False
    while not exit:
        if not greetUser():
            if registerAccount() == 1:
                print("your new account number is:", accountNumberGenerator(),"\nDo not share this number with anyone!")
                print("Your minimum deposit will be $1000")
                newAccountDeposit()
                break
            else:
                print("Have a good day")
                exit = True
                break
        elif greetUser():
            print("Good day2")
            exit = True
            break

main()
