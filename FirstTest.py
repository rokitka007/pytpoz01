import unittest
from Account import Account


class FirstTest(unittest.TestCase):

    def setUp(self):
        print("Set up test")
        # super()
        # self.account = Account("Arek", "10000001")

    def test_01_success(self):
        print("01")
        self.assertEqual(2, 2)

    def test_02_failure(self):
        print("02")
        self.assertEqual(2, 7)

    def tearDown(self):
        print("Lets clean")
        pass
