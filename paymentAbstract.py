from abc import ABC,abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay():
        pass

class UPI(Payment):
    def pay(self):
        print("Payment Done by UPI")

class CC(Payment):
    def pay(self):
        print("Payment Done by CC")

class DC(Payment):
    def pay(self):
        print("Payment Done by DC")

if __name__ == "__main__":
    u = UPI()
    u.pay()