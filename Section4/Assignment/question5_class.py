# Use a Random Number for the Account Number
import random

class SavingsAccount:

    # Declare all the Variables to be used throughout the Program
    def __init__(self, Name, PIN, AccountNumber, Balance):
        self.Name = Name
        self.PIN = PIN
        self.AccountNumber = AccountNumber
        self.Balance = Balance
    
    # Print Username
    def getName(self):
        print("User Name is: " + self.Name)
    
    # Print users PIN
    def getPIN(self):
        print("User PIN is: ", self.PIN)
    
    # Print Balance
    def getBalance(self):
        print("Current Balance is $", self.Balance)
    
    # Make a deposit
    def deposit(self):
        self.verifyInfo()
        transaction = int(input("Enter amount to Deposit: "))
        self.Balance += transaction
        print("Added ${} to the balance".format(transaction))
        print("New Balance is: $" , str(self.Balance))
    
    # Make a withdrawal
    def withdraw(self):
        self.verifyInfo()
        transaction = int(input("Enter amount to withdraw: $"))
        # Verify Balance is greater than requested withdrawl
        if self.Balance >= transaction:
            print("Withdrawal has been accepted.")
            self.Balance -= transaction
            print("New Balance is: $" , str(self.Balance))
        else:
            print("Insufficient funds available.")
    
    # Add interest to Balanace
    def computeInterest(self):
        self.verifyInfo()
        self.getBalance()
        print("Adding 0.02 interest to balance above...")
        self.Balance = self.Balance * (1 + 0.02)
        print("Current balance after interest is $", self.Balance )

    # Create the initial Account
    def createAccount():
        Name = input("Enter User Name: ")
        Balance = 0
        PIN = int(input("Enter PIN: "))

        # Generate an account number
        AccountNumber = random.randint(1,99999)
        print("User Account Number is: ", AccountNumber)
        return SavingsAccount(Name, PIN, AccountNumber, Balance)

    # Verify Account Number, and PIN. Both must match for account to be accessed.
    def verifyInfo(self):
        access = False
        while access == False:
            # Gather inputs to match
            AccountNumber = int(input("Please Enter your Account Number: "))
            PIN = int(input("Please Enter your PIN: "))
            # Check if Account Number matches
            if self.AccountNumber == AccountNumber:
                # Check if PIN matches
                if self.PIN == PIN:
                    # Grant Access
                    print("Account verified")
                    self.getBalance()
                    access = True
                else:
                    # Access denied, go back through while loop
                    print("Incorrect PIN")
            else:
                # Access denied, go back through while loop
                print("Incorrect Account Number")

