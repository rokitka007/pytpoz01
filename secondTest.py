import unittest
from unittest.mock import MagicMock, patch

from Account import Account
from Card import Card

class SecondTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account("Jan Kowalski", 1500)
        #self.account.getOwner = MagicMock(return_value="Piotr Nowak")

    def test_constructor(self):
        account = Account("Jan Kowalski", 1500)
        self.assertEqual(account.balance, 1500)
        self.assertEqual(account.owner, "Jan Kowalski")

    def test_01_getOwner(self):
        # owner = self.account.getOwner()
        self.assertEqual(,"Jan Kowalski")

       self.assertEqual(self.account.owner,"Jann Kowalski")


    def test_02_getBalance(self):
        self.assertEqual(self.account.balance, 1500)
        self.assertEqual(self.account.balance, 1000)

    def test_03_getNumber(self):
        return self.account.number

    def test_transfer_with_mock(self):
        self.account.balance = MagicMock(return_value=3000)
        self.assertEqual(self.account.balance.return_value, 1500)

    def test_transfer_with_patch(self):
        with patch.object(Account, "getBalance") as newBalance:
            newBalance.return_value = 0
            addedBalance = self.account.transfer(500)
            self.assertEqual(addedBalance,0)
            #self.assertEqual(newBalance.return_value, self.account.balance)
    def test_04_transfer(self):

        self.account.transfer(-500)
        self.account.balance

    def test_05_cardOwner(self):
        new_card_owner = self.card.owner()
        return self.account.owner

class CardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account("Jan Kowalski", 2000)
        self.card = Card(self.account,"1234")

    def test_owner(self):
        owner = self.card.owner()
        self.assertEqual(owner, self.account.getOwner())

    def test_account(self):
        self.assertEqual(self.card.get_account(), self.account.getNumber())

    def test_check_pin(self):
        self.assertTrue(self.card.check_pin("1234"))
        self.assertFalse(self.card.check_pin("5678"))



