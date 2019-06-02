import unittest

class FirstTest(unittest.TestCase):

    def setUp(self):                                    #tworzenie klasy na potrzeby testu
        print("Let's setUp test")
#        super()
#        self.account = Account("Bartosz","1100")

    def test_01_success(self):       #testy muszą mieć początek z nazwą test
        print("01")
        self.assertEqual(2,2)

    def test_02_failure(self):
        print("02")
        self.assertEqual(9,12)

    def tearDown(self):
        print("Let's cleanUp test")
        pass

#given when then    ciekawa sprawa sprawdź jak pisać i spróbuj - przejrzystość w formie pewnej historii

