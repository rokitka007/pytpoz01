import unittest
from unittest.mock import MagicMock
from Account import Account

class Accounttest(unittest.TestCase):

    def setUp(self):
        print("SetUp")
        self.account = Account("jan kowalski", 1500)
        # self.account.owner = MagicMock(return=value"Piotr Nowak") ???

    def test_constructors(self):
        account = Account("jan kowalski", 1500)
        self.assertEqual(account.balance, 1500)
        self.assertEqual(account.owner, "jan kowalski")

    def test_1_owner(self):
        owner = self.account.getOwner()
        self.assertEqual(owner, "jan kowalski")

    def test_2_balance(self):
        balance = self.account.getBalance()
        self.assertEqual(balance, self.account.getBalance()) #mozna tez 1500 na koniec

    def test_3_number(self):
        number = self.account.getNumber()
        self.assertEqual(self.account.number, self.account.getNumber())

    def test_4_transfer(self):
        new_balance = self.account.transfer(500)
        self.assertEqual(new_balance, 1000)

    def test_transferWithMock(self):
        self.account.balance = MagicMock(return_value=3000)
        self.assertEqual(self.account.balance.return_value, 1500)

    def test_transferWithPatch(self):
        with patch.object(Account, "getBalance") as newBalance:
            newBalance.return_value = 0
            addedBalance = self.account.transfer(500)

            self.assertEqual(addedBalance, 0)
            # self.accountEqual(newBalance.return_value, self.account.balance)
