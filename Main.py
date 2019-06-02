from Account import Account
from Card import Card


if "__main__" == __name__:
    acoount = Account("Jan Kowalski", 2583)
    card = Card(acoount, 1234)

    print("Account owner is: " + acoount.getOwner())
    print("Account number is: " + acoount.getNumber())
    acoount.transfer(1500)
    print("Account balance is: " + str(acoount.getBalance()))
    print("Card owner is: " + card.owner())
    print("Card account number is: " + card.get_account())
    card.check_pin(1234)
    card.check_pin(5678)
