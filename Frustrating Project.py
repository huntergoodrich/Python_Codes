class Accounts(object):
    def __init__(self, balance):
        self.balance = balance
        
    def depositing(self, amount):
        self.balance+= amount 
        print(self.balance)
        
    def withdrawing(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("You cannot do this right now.")
            
    def checking_balance(self):
        print(self.balance)
        
class Checking(Accounts):
    def withdrawing(self, amount):
        if 100 <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("You have insufficient funds")

    
class Savings(Accounts):
    def calc_interest(self):
        interest = self.balance * .01
        print(interest)




   
print("Welcome to Hunter Goodrich's ATM. ")
accountType = int(input("What type of account? 1:Savings; 2:Checking? "))
if accountType == 1:
    accountPicked = Savings(1500)
elif accountType == 2:
    accountPicked = Checking(1000)


repeat = "yes"
while repeat == "yes" or repeat == "Yes":
    menu = int(input("What do you want to do? 1:Deposit 2:Check Balance 3:Withdraw 4:Calculate Interest or 5:Exit "))
    if menu == 5:
        repeat = ("No")
        print("Have a nice day. ")
    elif menu == 1:
        amount_1 = int(input("How much money do you want to deposit? "))
        accountPicked.depositing(amount_1)
    elif menu == 2:
        accountPicked.checking_balance()
    elif menu == 3:
        amount = int(input("How much money do you want to take out? "))
        accountPicked.withdrawing(amount)
    elif menu == 4:
        accountPicked.calc_interest()


        
    
    
