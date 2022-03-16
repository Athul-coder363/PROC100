class Atm:
    def __init__(self,cardNumber) :
        self.cardNumber = cardNumber

    def Verify (self):
        yourCard = int(input("Please enterr you card number"))
        if self.cardNumber == yourCard:
            print("Verified")
        else:
            print("Wrong Number")
c1 = Atm(12345)
c1.Verify()
