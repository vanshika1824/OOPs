class Meal:
    def __cookRajma(self):
        print("Rajma Prepared")
    def __cookRice(self):
        print("Rice Prepared")
    def __preparesalaad(self):
        print("Salaad Prepared")
    def __cookRoti(self):
        print("Rice Prepared")
    def __Sweet(self):
        print("Sweet Prepared")

    def cookmeal(self):
        self.__cookRajma()
        self.__cookRice()
        self.__preparesalaad()
        self.__cookRoti()
        self.__Sweet()

if __name__ == "__main__":
    m = Meal()
    m.cookmeal()