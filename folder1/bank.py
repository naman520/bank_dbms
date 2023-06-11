#oops implementation for banking

class bank:
    def __init__(self,cname,cage,csex,amount,balance,acc_number=200):
        self.cname = cname
        self.cage = cage
        self.csex = csex
        self.acc_number = acc_number
        self.amount = amount
        self.balance = balance

    
    def enter(cls):
        print("***************************Enter Account Holder Details**********************************\n")
        cname = str(input("Account Holder Name :: "))
        cage = int(input("Age :: "))
        csex = str(input("Sex(M/F) :: "))
        return cls(cname,cage,csex)
        
    def show(self):
        print("\n\n***************************Showing Account Holder Details**********************************\n\n")
        print("Account Holder Name :: ",self.cname,"\n","Age :: ",self.cage,"\n","Sex :: ",self.csex)

account = bank.enter()
account.show()
account.money()