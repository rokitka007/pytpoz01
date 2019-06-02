import unittest
from Account import Account

class FirstTest(unittest.TestCase):

    def setUp(self):
        super()                                     #def __init__(self): i te komenty u góry
                                 #pass

    def test_01_success(self):
        print("01")
        self.assertEqual(2, 2)

    def test_02_failure(self):
        print("02")
        self.assertEqual(2, 7)

    def tearDown(self):
        print("Let's clean up")


