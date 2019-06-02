class Card():
    def __init__(self, account, pin):
        self.account = account
        self.pin = pin

    def owner(self):
        return self.account.owner

    def check_pin(self, pin):
        if pin==self.pin:
            print("Your pin is correct")
            return True
        else:
            print("Your pin is incorrect")
            return False

    def get_account(self):
        return self.account.number