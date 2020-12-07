# A class for the bank (one instance per game)

import math
from actor import Actor

class Bank(Actor):
    def __init__(self):
        """The bank's balance is unlimited, so we set it to 10 billion because we need a finite number.
        The bank initially owns all 32 houses and 12 hotels."""
        super().__init__(math.pow(10, 10), 32, 12)
        
    # The collect() and pay() methods from Actor are also inherited

    def sell_property(self, other, building = "house"):
        """Sell some number of houses or hotels to a player.
        Inputs are player and property type (house or hotel) as a string.
        Each house/hotel costs $100, but a hotel also requires 4 houses from that property and are traded in."""
        if building == "house":
            self.houses -= 1
            other.houses += 1
        elif building == "hotel":
            self.hotels -= 1
            other.hotels += 1
            other.houses -= 4
        self.balance += 100
        other.balance -= 100


