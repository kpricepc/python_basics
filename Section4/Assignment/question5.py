from question5_class import SavingsAccount

# Create User Account First
User1 = SavingsAccount.createAccount()

# Return User Account Information
User1.getName()
User1.getBalance()
User1.getPIN()

# Make a Deposit
print("Making a Deposit")
User1.deposit()

# Make a Withdraw
print("Making a Withdrawal")
User1.withdraw()

# Calculate Interest
print("Adding Interest")
User1.computeInterest()