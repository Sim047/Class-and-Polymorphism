# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protector of {self.city}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass demonstrating inheritance and polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):  # Polymorphism
        return f"{self.name} flies at {self.flight_speed} km/h using {self.power}!"

# Another subclass
class StrengthHero(Superhero):
    def __init__(self, name, power, city, strength_level):
        super().__init__(name, power, city)
        self.strength_level = strength_level

    def use_power(self):  # Polymorphism
        return f"{self.name} lifts objects with strength level {self.strength_level} using {self.power}!"

# Testing
hero1 = FlyingHero("SkyBlaze", "Wind Control", "Metroville", 500)
hero2 = StrengthHero("IronFist", "Super Strength", "Gotham", 9000)

print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())
