from abc import ABC,abstractmethod
#Multiple Inheritance

class Animal(ABC):
    @abstractmethod
    def sound():
        pass

class Bird(ABC):
    @abstractmethod
    def sound():
        print("Koo...Koo...")

    @abstractmethod
    def fly():
        pass

class Pigeon(Animal,Bird):
    def sound(self):
        print("Gutur Gu...Gutur Gu...")

    def fly(self):
        print("Flying....")

p = Pigeon()
p.sound()
p.fly()

from abc import ABC,abstractmethod
#Multiple Inheritance

class Animal(ABC):
    def sound(self):
        print("Gutur Gu...Gutur Gu...from Animal")

class Bird(ABC):
    def sound(self):
        print("Koo...Koo...from Bird")

    @abstractmethod
    def fly():
        pass

class Pigeon(Bird,Animal):
    def fly(self):
        print("Flying....")

p = Pigeon()
p.sound()
p.fly()


from abc import ABC,abstractmethod
#Multiple Inheritance

class Animal(ABC):
    def sound(self):
        print("Gutur Gu...Gutur Gu...from Animal")

class Bird(ABC):
    def sound(self):
        print("Koo...Koo...from Bird")

    @abstractmethod
    def fly():
        pass

class Pigeon(Animal,Bird):
    def fly(self):
        print("Flying....")

p = Pigeon()
p.sound()
p.fly()


