import unittest
import Account

class FirstTest(unittest.TestCase):

    def setUp(self):
        super()
        self.account = Account("Kasia", "2200")

    def test_01_success(self):
        print("01")
        self.assertEqual(2, 2)

    def test_02_failure(self):
        print("02")
        self.assertEqual(2, 7)

    def tearDown(self):
        pass