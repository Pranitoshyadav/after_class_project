from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, max_fule, max_speed):
        self.max_fule = max_fule
        self.max_speed = max_speed

    @abstractmethod
    def maxFule(self):
        pass

    @abstractmethod
    def maxSpeed(self):
        pass


class BMW(Car):
    def maxFule(self):
        print("Max fule is:", self.max_fule, "l")

    def maxSpeed(self):
        print("Max speed is:", self.max_speed, "km/h")


class Ferrari(Car):
    def maxFule(self):
        print("Max fule is:", self.max_fule, "l")

    def maxSpeed(self):
        print("Max speed is:", self.max_speed, "km/h")


oBMW = BMW(500, 100)
oFerrari = Ferrari(600, 110)

for car in (oBMW, oFerrari):
    car.maxFule()
    car.maxSpeed()

