import unittest
from unittest.mock import MagicMock

from Account import Account

class AccountTest(unittest.TestCase):

    def setUp(self):
        print('\nlets setup test')
        self.account = Account('yrek iksinski', 1000)
        self.account.owner = MagicMock(return_value='Piotr Nowak')
        self.number = self.account.number

    def test_01_owner(self):
        print('\n01 = Account.get_owner')
        print(self.account.getOwner())
        self.assertEqual(self.account.owner, self.account.getOwner())

    def test_02_balance(self):
        print('\n02 = Account.get_balance')
        print(self.account.getBalance())
        self.assertEqual(self.account.balance, self.account.getBalance())

    def test_03_number(self):
        print('\n03 = Account.get_number')
        print(self.account.number)
        self.assertEqual(self.account.number, self.account.getNumber())

    def test_04_transfer(self):
        print('\n04 = Account.transfer')
        self.transfer = self.account.transfer(500)
        self.assertEqual(self.account.balance, 1500)

    def tearDown(self):
        print('lets cleanUp test')