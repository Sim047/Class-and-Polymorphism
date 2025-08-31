# Class-and-Polymorphism
Week 5 assignment

"""
🐍 Python Programming Assignment

-----------------------------------------------
📘 Assignment 1: Design Your Own Class (Superhero)
🎭 Activity 2: Polymorphism Challenge (Vehicle)
-----------------------------------------------

✅ How to Use:

1. Make sure you have Python 3 installed.
2. Save this script as: assignment.py
3. Open your terminal or command prompt.
4. Run the script with:

    python assignment.py

🧾 This script demonstrates:
- Object-Oriented Programming (OOP)
- Classes, Constructors, Inheritance
- Polymorphism and Encapsulation
"""

# ==========================================================
# 🦸 Assignment 1: Superhero Class with Inheritance
# ==========================================================

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):  # Polymorphism
        return f"{self.name} flies at {self.flight_speed} km/h using {self.power}!"

class StrengthHero(Superhero):
    def __init__(self, name, power, city, strength_level):
        super().__init__(name, power, city)
        self.strength_level = strength_level

    def use_power(self):  # Polymorphism
        return f"{self.name} lifts objects with strength level {self.strength_level} using {self.power}!"

# === Superhero Demo ===

print("=== Superhero Demo ===")
hero1 = FlyingHero("SkyBlaze", "Wind Control", "Metroville", 500)
hero2 = StrengthHero("IronFist", "Super Strength", "Gotham", 9000)

print(hero1.introduce())
print(hero1.use_power())
print()
print(hero2.introduce())
print(hero2.use_power())

# =====================================================
# 🚗 Activity 2: Polymorphism Challenge - Vehicle Example
# =====================================================

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

# === Vehicle Demo ===

print("\n=== Vehicle Demo ===")
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())
