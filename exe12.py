
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
            return "PIN Verified",self.holder_name, self.acc_number
        else:
            return "Invalid PIN",self.holder_name, self.acc_number
        
    try:
        def deposit(self,amount):
            print("You are in deposit function")
            user_pin = input("Enter your PIN: ")
            self.user_pin = user_pin
            # print(self.user_pin)
            if self.user_pin != self.pin:
                # print("Invalid PIN")
                return "Invalid PIN",self.holder_name, self.acc_number
            else:
                # print("PIN Verified")
                self.amount = amount
                self.balance += self.amount
                print(f"{self.amount} rupees are successfully added to your account : {self.balance} = {self.balance - self.amount} + {self.amount} rupees")
    except:
        print("An error occurred during deposit.")
                
    try:
        def withdraw(self, amount):
            print("You are in withdraw function")
            user_pin = input("Enter your PIN: ")
            self.user_pin = user_pin
            if self.user_pin != self.user_pin:
                return "Invalid PIN",self.holder_name, self.acc_number
            else:
                self.amount = amount
                if self.amount > self.balance:
                    print("\nYour account don’t have sufficient balance ")
                else:
                    self.balance -= self.amount
                    print(f"{self.amount} rupees are successfully withdrawn from your account : {self.balance} = {self.balance + self.amount} - {self.amount} rupees")
    except:
        print("An error occurred during withdrawal.")
    
    
    def __str__(self):
        return f"Account Holder Name: {self.holder_name}\nAccount Number: {self.acc_number}\nAccount Balance: {self.balance} rupees"
        

account = BankAccount("Ram Kumar", "1234567890", 10000, "4321")

# print(account)
print()
account.deposit(200)
print()
print(account)
print()
account.withdraw(12000)
print()
account.withdraw(8000)
print()
print(account)

