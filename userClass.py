class User:
    def __init__(self, firstName, lastName, password, balance = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.balance = balance

    def describeUser(self):
        print("You are now a registered member of Axis Bank!")
        try:
            cont = int(input('''Would you like to see the details of your account?
Press 1 for yes
Press 2 for no'''))
            if cont == 1:
                print("First Name :", self.firstName,'\n'
'''Last Name :''', self.lastName)
            elif cont == 2:
                pass
        except (ValueError):
            print("Your entered a string")
