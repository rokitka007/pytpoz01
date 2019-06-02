import unittest
from unittest.mock import MagicMock, patch
from Account import Account
from Card import Card


class SecondTest(unittest.TestCase):

    def setUp(self):
        print("Set up test")
        # super()
        self.account = Account("Jan Kowalski", 2583)
        self.card = Card(self.account, 4083)
        # self.account.owner = MagicMock(return_value-"Piotr Nowak")

    def test_01_Get_owner(self):
        print("Account get owner")
        self.assertEqual(self.account.getOwner(), self.account.owner)  # mozna zamiast self.account.owner wpisać konretne azwisko
        # # self.account.owner = MagicMock(return_value-"Piotr Nowak")
        # with patch.object(Account, "owner") as acow:
        #     acow.return_value = "Kazimierz"
        #     self.assertEqual("Jan Kowalski", self.account.owner)

    def test_02_Get_ballance(self):
        print("Account get ballance")
        self.assertEqual(self.account.getBalance(), 2583)

    def test_03_number(self):
        print("Account number")
        self.assertEqual(self.account.getNumber(), self.account.number)  #porównuje to samo.. nie ma sensu, bo nie jest predefiniowane, bo predefiniowane jest generatorem

    def test_04_transfer(self):
        print("Account transfer")
        self.assertEqual(self.account.transfer(-1000), 1583)

    def test_05_transfer_failure(self):
        new_balance = self.account.transfer(1500)  # jesli wywala, to znaczy ze setup predefiniuje do kazdej metody od nowa
        self.assertEqual(new_balance, 4083)
        # return self.getBalance()

    def test_transferWithMock(self):
        self.account.balance = MagicMock(return_value=3000)
        self.assertEqual(self.account.balance.return_value, 1500)

    def test_transferWithPatch(self):
        with patch(Account, "getBalance") as newBalance:   # witch - działa tylko pod tym with  # ALT + ENTER NA PATCHU I ZAIMPORTUJ GO BY DZIAŁał
            newBalance.return_value = 0
            addedBalance = self.account.transfer(500)

            self.assertEqual(addedBalance, 0)
            # self.assertEqual(newBalance.return_value, self.account.balance)

    def test_05_Card_owner(self):
        print("Account owner")
        self.assertEqual(self.card.owner(), self.account.owner)

    def test_06_Card_check_pin(self):
        print("Card check pin")
        self.assertTrue(self.card.check_pin(4083))

    def test_07_Card_get(self):
        print("card get")
        self.assertTrue(self.card.get_account(), self.account.getNumber())

    def tearDown(self):
        print("Lets clean")
        pass


