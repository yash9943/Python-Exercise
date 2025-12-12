
class BankAccount:
    def __init__(self, holder_name,acc_number,balance,pin):
        self.holder_name = holder_name
        self.acc_number = acc_number
        self.balance = balance
        self.pin = pin
        
        
    def check_pin(self):
        enter_pin = input("Enter your PIN: ")
        self.enter_pin = int(enter_pin)
        if self.enter_pin == self.pin:
            return True
        else:
            return False
        
    try:
        def deposit(self,amount):
            pin_verification = account.check_pin()
            if pin_verification == True:
                # print("You are in if block of deposit function")
                self.amount = amount
                self.balance += self.amount
                print(f"{self.amount} rupees are successfully added to your account : {self.balance} = {self.balance - self.amount} + {self.amount} rupees")
            else:
                # print("You are in else block of deposit function")
                print("Invalid PIN")
    except:
        print("An error occurred during deposit.")
                
    try:
        def withdraw(self, amount):
            pin_verification = account.check_pin()
            if pin_verification == True:
                self.amount = amount
                if self.amount > self.balance:
                    print("\nYour account don’t have sufficient balance ")
                else:
                    self.balance -= self.amount
                    print(f"{self.amount} rupees are successfully withdrawn from your account : {self.balance} = {self.balance + self.amount} - {self.amount} rupees")
            else:
                print("Invalid PIN")

    except:
        print("An error occurred during withdrawal.")
    
    def __str__(self):
        return f"Account Holder Name: {self.holder_name}\nAccount Number: {self.acc_number}\nAccount Balance: {self.balance} rupees"
        

account = BankAccount("Ram Kumar", "1234567890", 10000, 4321)

print("---Account Details---")

print(account)
print("---Deposit---")
account.deposit(200)
print()
print(account)
print("---Withdraw---")
account.withdraw(12000)
print()
account.withdraw(8000)
print()
print(account)