from bank_account import BankAccount

customer_1 = BankAccount()
customer_1.deposit(10000)
customer_1.withdraw(5000)

print(customer_1.checkBalance())

"""Private attributes are not accessable 
through another file unless a getter method is used"""