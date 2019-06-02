import unittest
from Account import  Account
from Card import Card

class FirstTest(unittest.TestCase):

    def setUp(self):
        print('lets setup test')

    def test_01_success(self):
        print('01')
        self.assertEqual(2,2)

    def test_02_ao(self):
        print('Account.get_owner')
        print(Account.getOwner(self,))

    def test_02_failure(self):
        print('02')
        self.assertEqual(2,2)

    def tearDown(self):
        print('lets cleanUp test')