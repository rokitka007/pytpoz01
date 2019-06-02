from random import randint

class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.number = ""
        for i in range(26):
            self.number += str((randint(0, 9)))

    def getOwner(self):
        return self.owner

    def getBalance(self):
        return self.balance

    def getNumber(self):
        return self.number

    def transfer(self, amount):
        self.balance += amount
        print("Your balance changed: " + str(self.balance))
        return self.getBalance()
