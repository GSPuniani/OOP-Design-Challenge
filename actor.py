# Abstract class from which Bank and Player inherit

from abc import ABC, abstractmethod

class Actor(ABC):

    def __init__(self, balance = 0, houses = 0, hotels = 0):
        """Each actor has a balance, a number of houses, and a number of hotels."""
        self.balance = balance
        self.houses = houses
        self.hotels = hotels

    # The collect() and pay() methods are used for many types of transactions between actors (rent, salaries, etc.)

    def collect(self, other, amount):
        """Transfer money from another actor to self."""
        self.balance += amount
        other.balance -= amount
    
    def pay(self, other, amount):
        """Transfer money to another actor from self."""
        self.balance -= amount
        other.balance += amount

    # Banks and players have their own versions of sell_property()
    @abstractmethod
    def sell_building(self):
        pass
