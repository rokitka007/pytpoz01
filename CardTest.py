import unittest
from Account import Account
from Card import Card

class CardTest(unittest.TestCase):

    def setUp(self):
        print('\nlets setup test')
        self.account = Account('yrek iksinski', 1000)
        self.card = Card(self.account, 1234)

    def test_01_card_owner(self):
        print('\n01 - card owner')
        print(self.card.owner())
        self.assertEqual(self.card.owner(), self.account.owner)

    def test_02_check_pin(self):
        print('\n02 - check pin')
        self.card.check_pin(self.card.pin)
        self.assertEqual(self.card.pin, 1234)

    def test_03_get_account(self):
        print('\n03 - get account')
        print(self.card.account.number)
        self.assertEqual(self.card.account.number, self.account.number)

    def tearDown(self):
        print('lets cleanUp test')