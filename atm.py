class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
    def menu(self):
        user_input=input("""
        welcome to the bank
        how would you like to procced?
        1. press 1 to create pin
        2. press 2 to deposite
        3. press 3 to withdraw
        4. press 4 to check balance
        5. press 5 to exit
        """)
        
        if user_input == '1':
            self.create_pin()
            
        if user_input == '2':
            self.deposite()
            
        if user_input == '3':
            self.withdraw()
            
        if user_input == '4':
            self.check_balance()
            
        if user_input == '5':
            self.exit()
            
    def create_pin(self):
        self.pin=input("enter pin:")
        print("pin set successfully")
        self.menu()
        
    def deposite(self):
        temp=input("enter pin:")
        if temp == self.pin:
            amount=int(input("enter the amount:"))
            self.balance=self.balance+amount
            print("deposite successfully")
        else:
            print("invalid pin")
        self.menu()
            
    def withdraw(self):
        temp=input('enter pin:')
        if temp == self.pin:
            amount=int(input("enter the amount to withdraw"))
            if amount < self.balance:
                self.balance=self.balance-amount
                print("withdrawal successfully")
            else:
                print("low balance")
        else:
            print("invalid pin")
        self.menu()
        
    def check_balance(self):
        temp=input("enter pin:")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")
        self.menu()
            
    def exit(self):
        pass
        
        
obj=Atm()
obj.menu()


print("helloo prasad")
    