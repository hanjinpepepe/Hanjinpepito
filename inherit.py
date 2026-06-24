from oop import Vehicle  

# Inheretance
class Car(Vehicle):
    def move(self):
        print(f"The {self.brand} car is moving at {self.speed} km/h.")
        
class Motorcycle(Vehicle):
    def move(self):
        print(f"The {self.brand} motorcycle is moving at {self.speed} km/h.")
        