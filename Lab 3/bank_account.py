class BankAccount:
    def __init__(self):
        self.__balance = 0
        ## Use (__) infront of an attribute to make an attribute private. 

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("You don't have sufficient balance!")

    ## Getter method for accessing private variables.
    def checkBalance(self):
        return self.__balance