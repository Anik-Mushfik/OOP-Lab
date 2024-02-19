class Account:
    def __init__(self, name, contact, balance):
        self.name = name
        self.contact = contact
        self.balance = balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def deposit(self, amount):
        self.balance = self.balance + amount
    
A1 = Account("Fahim", "01961905838", 5000)
print(A1.name)
print(A1.contact)
print(f"Balance: {A1.balance}")
A1.withdraw(2000)
print(f"New Balance: {A1.balance}")
A1.deposit(500)
print(f"New Balance: {A1.balance}")