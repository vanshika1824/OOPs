class Bank:
    __accno = 0   #private variable using __ double underscore
    __name = ""
    __balance = 0

    def __init__(self,accno,name,bal):
        self.__accno = accno
        self.__name = name
        self.__balance = bal

    def getaccno(self):
        return self.__accno
    
    def setaccno(self,accno):
        self.__accno = accno

    def getname(self):
        return self.__name
    
    def setname(self,name):
        self.__name

    def getbal(self):
        return self.__balance

    def setbal(self,bal):
        self.__balance

b = Bank(284736,"vanshika",2308495)

print(b._Bank__accno)    #name mangling
print(b.getaccno())
print(b.getname())
print(b.getbal())
b.setaccno("A5747")
print(b.getaccno())


