'''Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.'''

class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return ("Owner: %s ; Balance: %s" % (self.owner, self.balance))
    
    def __del__(self):
        print("Account deleted")
    
    def deposit(self):
        while True:
            amt_dep = int(input("How much would you like to deposit %s? " % (self.owner)))
            if amt_dep > 0:
                self.balance += amt_dep
                print("You deposited $%s into your bank account. \nYour balance is : $%s" % (amt_dep,self.balance))
                break
            else:
                print('Please enter a valid amount to deposit')
                continue
        
    def withdraw(self):
         while True:
            amt_with = int(input("How much would you like to withdraw {}? ".format(self.owner)))
            if amt_with > 0:
                if amt_with <= self.balance:
                    self.balance -= amt_with
                    print("You withdrew $%s from your bank account. \nYour balance is : $%s" % (amt_with,self.balance))
                    break
                else:
                    print("Sorry, you do not have enough in your account to withdraw that amount. Please enter a valid amoount")
                    continue
            else:
                print('Please enter a valid amount to withdraw')
                continue
                
def use_bank(self):
    while True:
        while True:
            w_or_d = input("Would you like to withdraw or deposit %s? " % (self.owner))
            if w_or_d in ['w','W','withdraw','d','D','deposit']:
                break
            else:
                print('Please provide a valid response.')
                continue
        if w_or_d in ['w','W','withdraw']:
            self.withdraw()
            while True:
                cont = input('Would you like to continue using the bank?')
                if cont in ['y','yes','n','no']:
                    break
                else:
                    print('Please provide a valid response.')
                    continue
            if cont in ['y','yes']:
                continue
            else:
                break
        else:
            self.deposit()
            while True:
                cont = input('Would you like to continue using the bank?')
                if cont in ['y','yes','n','no']:
                    break
                else:
                    print('Please provide a valid response.')
                    continue
            if cont in ['y','yes']:
                continue
            else:
                break
            
    
