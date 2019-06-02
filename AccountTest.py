import unittest
from unittest.mock import MagicMock, patch

from Account import Account
from Card import Card

class AccountTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(cls)
        cls.account2 = Account("Piotr Nowak", 1500)

    def setUp(self):
        print("SetUp account")
        self.account = Account("Jan Kowalski", 1500)
        self.account.owner = MagicMock(return_value="Piotr Nowak")

    def test_constructor(self):
        self.assertEqual(self.account.balance, 1500)
        self.assertEqual(self.account.owner, "Jan Kowalski")

    def test_getOwner(self):
        self.assertEqual(self.account.owner.return_value, "Jan Kowalski")

    def test_getOwner2(self):
        with patch.object(Account, "getOwner") as acow:
            acow.return_value = "Kazimierz"

            self.assertEqual(self.account.owner, acow.return_value)

    def test_getBalance(self):
        balance = self.account.getBalance()

        self.assertEqual(balance, 1500)

    def test_transfer(self):
        new_balance = self.account.transfer(-500)
        # self.account2.transfer(-500)

        self.assertEqual(new_balance, 1000)

    def test_transfer_failure(self):
        new_balance = self.account.transfer(500)

        self.assertEqual(new_balance, 1500)

    def test_transfer_success(self):
         new_balance = self.account2.transfer(500)

         self.assertEqual(new_balance, 1500)

    def test_transferWithMock(self):
        self.account.balance = MagicMock(return_value=3000)

        self.assertEqual(self.account.balance.return_value, 1500)

    def test_transferWithPatch(self):
        with patch.object(Account, "getBalance") as newBalance:
            newBalance.return_value = 0
            addedBalance = self.account.transfer(500)

            self.assertEqual(addedBalance, 0)
            # self.assertEqual(newBalance.return_value, self.account.balance)

class CardTest(unittest.TestCase):
    def setUp(self):
        self.account = Account("Hej Hej", 2106)
        self.card = Card(self.account, "1234")

    def test_owner(self):
        owner = self.card.owner()

        self.assertEqual(owner, self.account.getOwner())

    def test_account(self):
        self.assertEqual(self.card.get_account(), self.account.getNumber())

    def test_checkPin(self):
        self.assertTrue(self.card.check_pin("1234"))
        self.assertFalse(self.card.check_pin("5879"))

