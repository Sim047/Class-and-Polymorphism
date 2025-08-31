class Vehicle:
    def move(self):
        return "The vehicle moves."

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# List of vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for v in vehicles:
    print(v.move())
