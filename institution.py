class Institution:
    def __init__(self, institutionId, institutionName, noofstudentsplaced, noofstudentscleared, location):
        self.__institutionId = institutionId
        self.__institutionName = institutionName
        self.__noofstudentsplaced = noofstudentsplaced
        self.__noofstudentscleared = noofstudentscleared
        self.__location = location
        self.__grade = None

    def getinstitutionId(self):
        return self.__institutionId

    def getInstitutionName(self):
        return self.__institutionName

    def getNoofstudentsplaced(self):
        return self.__noofstudentsplaced

    def getNoofstudentscleared(self):
        return self.__noofstudentscleared

    def getLocation(self):
        return self.__location

    def getGrade(self):
        return self.__grade

    def setGrade(self, grade):
        self.__grade = grade


class Solution:

    @staticmethod
    def FindNumClearancedByLoc(institutions, location):
        total = 0
        for inst in institutions:
            if inst.getLocation().lower() == location.lower():
                total += inst.getNoofstudentscleared()
        return total

    @staticmethod
    def UpdateInstitutionGrade(institutions, institutionName):
        for inst in institutions:
            if inst.getInstitutionName().lower() == institutionName.lower():
                placed = inst.getNoofstudentsplaced()
                cleared = inst.getNoofstudentscleared()

                rating = (placed * 100) // cleared

                if rating >= 80:
                    inst.setGrade('A')
                else:
                    inst.setGrade('B')

                return inst
        return None


# -------- MAIN --------
if __name__ == "__main__":
    institutions = []

    for _ in range(4):
        institutionId = int(input())
        institutionName = input()
        noofstudentsplaced = int(input())
        noofstudentscleared = int(input())
        location = input()

        institutions.append(
            Institution(institutionId, institutionName, noofstudentsplaced, noofstudentscleared, location)
        )

    location_input = input()
    institutionName_input = input()

    print("-----------output-----------")

    total_cleared = Solution.FindNumClearancedByLoc(institutions, location_input)

    if total_cleared > 0:
        print(total_cleared)
    else:
        print("There are no cleared students in this particular location")

    result = Solution.UpdateInstitutionGrade(institutions, institutionName_input)

    if result is not None:
        print(result.getInstitutionName() + "::" + result.getGrade())
    else:
        print("No Institution is available with the specified name")