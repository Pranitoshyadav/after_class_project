class Vehicle:
    def __init__(self, seats):
        self.seats = seats

    def total_fare(self):
        # Base fare: seats × 100
        return self.seats * 100


class Bus(Vehicle):
    def __init__(self, seats):
        super().__init__(seats)

    def total_fare(self):
        base_fare = super().total_fare()
        return base_fare + (0.1 * base_fare)



bus = Bus(50)
print("Total Bus Fare:", bus.total_fare())
