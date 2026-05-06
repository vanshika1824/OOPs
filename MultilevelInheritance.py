from abc import ABC,abstractmethod
#Multilevel Inheritance

class Animal(ABC):
    @abstractmethod
    def sound():
        pass

class Bird(Animal,ABC):
    @abstractmethod
    def fly():
        pass

class Pigeon(Bird):
    def sound(self):
        print("Gutur Gu...Gutur Gu...")

    def fly(self):
        print("Flying....")

p = Pigeon()
p.sound()
p.fly()