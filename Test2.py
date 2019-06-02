import unittest
from unittest.mock import MagicMock, patch
from Account import Account
from Card import Card

class SecondTest(unittest.TestCase):
    def setUp(self):                                #przy każdym teście resetuje wartości wejściowe
        print("SetUpTest")
        self.account = Account("Jan Kowalski", 2580)
        self.card = Card(self.account, 1234)

    def tearDown(self):
        print("TearDown")

    def test_01_get_owner(self):
        print("GET OWNER")
        self.assertEqual(self.account.getOwner(),"Jan Kowalski")

    def test_02_get_balance(self):
        print("GET BALANCE")
        self.assertEqual(self.account.getBalance(),2580)

    def test_03_get_number(self):
        print("GET NUMBER")
        self.assertEqual(len(self.account.getNumber()),26)
        self.assertEqual(self.account.getNumber(),self.account.number)

    def test_04_1_Account_transfer(self):
        print("ACCOUNT TRANSFER")
        self.assertEqual(self.account.transfer(2000),4580)

    # def test_04_2_Account_transfer(self):
    #     print("ACCOUNT TRANSFER WITH MOCK")
    #     self.account.balance = MagicMock(return_value=3000)
    #     self.assertEqual(self.account.balance.return_value, 1500)

    def test_04_3_Account_transfer(self):
        print("ACCOUNT TRANSFER WITH PATCH")
        with patch.object(Account, "getBalance") as newBalance:
            newBalance.return_value=0
            self.assertEqual(newBalance, self.account.balance)

    def test_05_card_owner(self):
        print("CARD OWNER TEST")
        self.assertEqual(self.account.getOwner(),self.card.owner())

    def test_06_card_check_pin(self):
        print("PIN TEST")
        self.assertTrue(self.card.check_pin(1234))
        self.assertFalse(self.card.check_pin(5478))

    def test_07_card_get_account(self):
        print("Card Number Check")
        self.assertEqual(self.account.getNumber(),self.card.get_account())

