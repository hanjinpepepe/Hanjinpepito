from abc import ABC, abstractmethod
from turtle import speed

class Vehicle(ABC):
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
    def get_speed(self):
        return self.__speed #Encapsulation: Private attribute
    
    #Getter Method
    def get_speed(self):
        return self.__speed
    
    #Setter Method
    def set_speed(self, speed):
        self.__speed = speed
        
    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed
        else:
            print("Speed cannot be negative!")
    
    @abstractmethod
    def move(self):
        pass 