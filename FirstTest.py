import unittest


class FirstTest(unittest.TestCase):
    def setUp(self):
        print("Lets setUp test")

    def test_01_success(self):
        print("01")
        self.assertEqual(2, 2)

    def test_01_failure(self):
        print("02")
        self.assertEqual(2, 3)

    def tearDown(self):
        print("Lets clearUp test")