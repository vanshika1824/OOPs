class TravelAgencies:
    __regNo = 0
    __agencyName = ""
    __packageType = ""
    __price = 0
    __flightFacility = False

    def __init__(self,regNo,agencyName,packageType,price,flightFacility):
        self.__regNo = regNo
        self.__agencyName = agencyName
        self.__packageType = packageType
        self.__price = price
        self.__flightFacility = flightFacility

    def getregNo(self):
        return self.__regNo
    def setregNo(self,regNo):
        self.__regNo = regNo

    def getagencyName(self):
        return self.__agencyName
    def setagencyName(self,agencyName):
        self.__agencyName = agencyName

    def getpackageType(self):
        return self.__packageType
    def setpackageType(self,packageType):
        self.__packageType = packageType

    def getprice(self):
        return self.__price
    def setprice(self,price):
        self.__price = price

    def getflightFacility(self):
        return self.__flightFacility
    def setflightFacility(self,flightFacility):
        self.__flightFacility = flightFacility

class Solution:
    @staticmethod
    def findAgencyWithHighestPackagePrice(lst):
        max = 0
        for agency in lst:
            if agency.getprice()>max:
                max = agency.getprice()
        
        return max
    
    @staticmethod
    def agencyDetailsForGivenIdAndType(lst,regNo,packageType):
        for agency in lst:
            if agency.getflightFacility() and agency.getregNo() ==regNo and agency.getpackageType() == packageType:
                return agency
        return None    

if __name__ == "__main__":
    n = int(input())
    lst=[]
    for i in range(n):
        regNo = int(input())
        agencyName = input()
        packageType = input()
        price = int(input())
        flightFacility = bool(input())

        agency = TravelAgencies(regNo,agencyName,packageType,price,flightFacility)
        lst.append(agency)

    regNo = int(input())
    packageType = input()

    print("------------------------------------\nOutput\n--------------------------------------")
    max = Solution.findAgencyWithHighestPackagePrice(lst)
    agency = Solution.agencyDetailsForGivenIdAndType(lst,regNo,packageType)

    print(max)
    print(agency.getagencyName(),":",agency.getprice())