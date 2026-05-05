class Bank:
    accno = 0
    name = ""

    def __init__(self,accno,name): #with constructor
        self.accno = accno
        self.name = name

    def show(self):    #without constructor
        print("Account no.:",self.accno)
        print("Name:",self.name)

b = Bank(599980,"Vanshika Maru")
b2 = Bank(588970,"Sakshi Goyal")
print(b.name)
b.show()
b2.show()
