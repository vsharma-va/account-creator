from userClass import User
import string
import random

'''----------------------------------------------------------------------------------------------------------------------------------------------
                                                All the file operation
----------------------------------------------------------------------------------------------------------------------------------------------'''

#Opens the file where the pins are stored
def openRegisteredPins():
    with open("L:\\Python Projects\\Updated Bank Program\\bankaccount\\bankaccount\\registeredPins.txt", 'r') as file:
        pins = file.readlines()
    file.close()
    return pins


#Opens the file where the bank balance is stored
def openBankBalance():
    with open("L:\\Python Projects\\Updated Bank Program\\bankaccount\\bankaccount\\bankbalance.txt", 'r') as file:
        accountBalance = file.readlines()
    file.close()
    return accountBalance


#appends/writes on the files
#takes takes 4 optional parameters. first parameter is the first name and the pin seperated by a space
#second parameter is the bank balance. Third parameter is the position of the account in the file. As bank balance on line 1 will belong to Roy
#Fourth parameter is a bool asking whether to append or write(False->append, True->Write)
def writeFile(data = '', balance = 0, position = 0, reWrite: bool = False):
    if data != '':
        with open("L:\\Python Projects\\Updated Bank Program\\bankaccount\\bankaccount\\registeredPins.txt", 'a') as file:
            file.write( data)
        file.close()

    if balance != 0 and not reWrite:
        with open("L:\\Python Projects\\Updated Bank Program\\bankaccount\\bankaccount\\bankbalance.txt", 'a') as file:
            file.write(str(balance))
        file.close()

    elif balance != 0 and reWrite:
        with open("L:\\Python Projects\\Updated Bank Program\\bankaccount\\bankaccount\\bankbalance.txt", 'r+') as file:
            accountInfo = cleanList()
            accountBalance = accountInfo[1]
            accountBalance[position] = str(balance)
            for element in accountBalance:
                file.write(element)
                file.write('\n')
            
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


def cleanList():
    cleanListPins = removeSpaces(removePunctuation(openRegisteredPins()))
    cleanListBalance = removeSpaces(removePunctuation(openBankBalance()))
    return cleanListPins, cleanListBalance


'''---------------------------------------------------------------------------------------------------------------------------------------------
                                                Account Registeration/Account Checker
---------------------------------------------------------------------------------------------------------------------------------------------'''

#Checks whether the user is registered or not
def greetUser():
    registeredPins = cleanList()                                        #cleanList function returns registered pin list and balance list as tuple                    
    userInDataBase: bool = False
    lenRegisteredPins = len(registeredPins)
    elementIndex = 0
    chances = 3                                                         #Amount of chances user gets to enter his/her correct information
    index = 0
    print("Welcome to Axis Bank\n")

    try:
        registered = int(input('''Are you registered with us?
press 1 for yes
press 2 for no\n'''))
    except TypeError:
        print("Entered a string")
    if registered == 1:
        for i in range(chances):
            if not userInDataBase:
                userName = input("Enter your registered name: ")
                userPin = input("Enter your registered Pin: ")
                for z in registeredPins[0]:
                    search = userName + ' ' + userPin
                    if search == z:
                        print("Welcome")
                        userInDataBase = True
                        index = registeredPins[0].index(z)               #returns the index of the account to be used to update bank balance later
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
            else:
                break
    elif registered == 2:
        print("would you like to register?")
        userInDataBase = False
    return userInDataBase, index


#Process to register an account
def registerAccount():
    registeredPins = cleanList()
    correct: bool = False
    enterNameAgain: bool = False
    numberOfTries: int = 0 
    try:
        wantsAccount = int(input("Press 1 to register a account "+"\nPress 2 to exit \n"))  
    except TypeError:
        print("You entered a string") 
    if wantsAccount == 1:
        while not correct:
            if enterNameAgain or numberOfTries == 0:
                firstName = input("Enter your first name: ")
                lastName = input("Enter your last name: ")
                pin = input("Enter your desired Pin (Must be 4 integers): ")
            else:
                pin = input("Enter your desired Pin (Must be 4 integers): ")

            if inputChecker(firstName, 2) and inputChecker(lastName, 2) and inputChecker(pin, 4, 1):#input checker function checks the length of input                
                rePin = input("Enter your pin again for conformation: ")
                if rePin == pin:
                    correct = True
                    newUser = User(firstName, lastName, pin)  # fills the input to the User class in the file userClass.py in the same directory
                    newUser.describeUser()
                    userData = firstName + ' ' + pin
                    registeredPins[0].append(userData)
                    writeFile(userData)                        #writes the info on the file
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


#input checker function thakes two parameters and one optional parameter
#first parameter is the data whose length needs to be checker. Second parameter is the length, data should be equal or greater than
#Third parmeter if equal to one then the length of data must be equal to the second parameter
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


# random account generator which cannot have 0 as the first digit
def accountNumberGenerator():
    accountLength = 10
    newAccountNumber = ""
    for i in range(0, accountLength, 1):
        if i == 0:
            digit = str(random.randint(1, 9))
            newAccountNumber += digit
        else:
            digit = str(random.randint(0, 9))
            newAccountNumber += digit
    return int(newAccountNumber)

'''----------------------------------------------------------------------------------------------------------------------------------------
                                                            Account operations
----------------------------------------------------------------------------------------------------------------------------------------'''                                                             

#takes in the index from greetUser() function
def depositAmount(indexValue):
    amountToDeposit = float(input("Enter the amount to deposit: "))
    accounts = cleanList()
    currentBalance = float(accounts[1][indexValue])
    finalBalance = amountToDeposit + currentBalance
    writeFile('', finalBalance, indexValue, True)
    print("Your current Balance is $", finalBalance)


def withdrawAmount(indexValue):
    amountToWithdraw = float(input("Enter the amount you want to withdraw: "))
    accountInfo = cleanList()
    accountBalance = accountInfo[1]
    currentBalance = float(accountBalance[indexValue])
    if currentBalance - amountToWithdraw >= 1000:
        finalBalance = currentBalance - amountToWithdraw
        writeFile('', finalBalance, indexValue, True)
        print("Your current Balance is $", finalBalance)
    elif currentBalance - amountToWithdraw <= 1000:
        print("You dont have enough balance to withdraw", amountToWithdraw)


def transferAmount(indexValue):
    amountToTransfer = float(input("Enter the amount you want to transfer: "))
    accountInfo = cleanList()
    accountBalance = accountInfo[1]
    currentBalance = float(accountBalance[indexValue])
    if currentBalance - amountToTransfer >= 1000:
        finalBalance = currentBalance - amountToTransfer
        writeFile('', finalBalance, indexValue, True)
        print("Your current Balance is $", finalBalance)
    elif currentBalance - amountToTransfer <= 1000:
        print("You dont have enough balance to transfer", amountToTransfer)


def checkBalance(indexValue):
    accountInfo = cleanList()
    accountBalance = accountInfo[1]
    currentBalance = float(accountBalance[indexValue])
    print("Your current balance is", currentBalance)


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
    return balance


def userChoice():
    print("What would you like to do?\n")
    try:
        userInput = int(input('''Enter 1 to deposit
Enter 2 to withdraw
Enter 3 to transfer
Enter 4 to check balance\n'''))
    except TypeError:
        print("Entered a string")
    returnVariable = ''
    if userInput == 1:
        returnVariable = "Deposit"
    elif userInput == 2:
        returnVariable = "Withdraw"
    elif userInput == 3:
        returnVariable = "Transfer"
    elif userInput == 4:
        returnVariable = "checkBalance"
    else:
        returnVariable = "invalid"
    return returnVariable

'''----------------------------------------------------------------------------------------------------------------------------------------'''

def main():
    exit: bool = False
    registeredUser, index = greetUser()
    while not exit:
        if not registeredUser:
            if registerAccount():
                print("your new account number is:", accountNumberGenerator(), "\nDo not share this number with anyone!")
                print("Your minimum deposit will be $1000")
                print("Enter amount to deposit: ")
                writeFile('',newAccountDeposit())
                break
            else:
                print("Have a good day")
                exit = True
                break
        elif registeredUser:
            usersChoice = userChoice()
            if usersChoice == "Deposit":
                depositAmount(index)
            elif usersChoice == "Withdraw":
                withdrawAmount(index)
            elif usersChoice == "Transfer":
                transferAmount(index)
            elif usersChoice == "checkBalance":
                checkBalance(index)   
            break
        
main()
