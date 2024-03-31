class Account:
    ID = 1000
    def __init__(self, user_name:str):
        self.user_name = user_name
        self.__balance = 500
        self.transactions = []
        Account.ID += 1

    def withdraw(self, amount:float, date:int):
        if self.__balance >= amount:
            self.__balance -= amount
            transaction_no = len(self.transactions)+1
            transaction = Transaction("Withdraw", amount, date, transaction_no)
            self.transactions.append(transaction)
        else: raise InSufficiantBalanceError(self.get_balance(), amount)

    def deposite(self, amount:float, date:str):
        self.__balance += amount
        transaction_no = len(self.transactions)+1
        transaction = Transaction("Deposite", amount, date, transaction_no)
        self.transactions.append(transaction)

    def get_balance(self):
        return self.__balance


class Transaction:
    def __init__(self, type:str, amount:float, date, transaction_no):
        self.type = type
        self.amount = amount
        self.date = date
        self.transaction_no = transaction_no 

    def __repr__(self):
        return f"Transaction No: {self.transaction_no}; Type: {self.type}; Amount: {self.amount}"
    

class InSufficiantBalanceError(Exception):
    def __init__(self, account_balance, withdrawal_balance):
        self.account_balance = account_balance
        self.withdrawal_balance = withdrawal_balance
    

ac_1 = Account(123)
ac_1.deposite(50000, "12/5")
ac_1.withdraw(10000, "13/5")
print(ac_1.get_balance())
print(ac_1.transactions)

ac_2 = Account(123)
ac_2.deposite(10000, "12/5")
try:
    ac_2.withdraw(20000, "12/5")
except InSufficiantBalanceError as error:
    print(f"Not Enough Balance: Account balance {error.account_balance} is less than Withdrawal balance {error.withdrawal_balance}")
print(ac_2.get_balance())
print(ac_2.transactions)