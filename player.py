# A class for each player of the game

import random
from actor import Actor

class Player(Actor):
    def __init__(self, token):
        """Initialize a player with a token of their choosing. 
        Every player begins with $1500, 0 houses, and 0 hotels at the start of the game."""
        super().__init__(1500)
        self.token = token
        self.position = 0
        self.properties = []

    # The collect() and pay() methods from Actor are also inherited
    
    def roll_dice(self):
        """Roll two standard dice. Return a tuple of the roll"""
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"{die1}, {die2}")
        if die1 == die2:
            print("Doubles!")
        return (die1, die2)

    def sell_building(self, other, building = "house"):
        """Sell some number of houses or hotels back to the bank.
        Inputs are player and property type (house or hotel) as a string.
        Each house/hotel costs $100, but the bank only buys them back at half-value."""
        if building == "house":
            self.houses -= 1
            other.houses += 1
        elif building == "hotel":
            self.hotels -= 1
            other.hotels += 1
            self.houses += 4
            other.houses -= 4
        self.balance += 50
        other.balance -= 50

    # Move token
    def move_token(self):
        """Advance token by number indicated in dice roll. Reset position as the token completes a circuit.
        A double roll begets another turn rolling the dice."""
        # `roll` is a tuple with two values from the dice roll
        roll = self.roll_dice()
        self.position += sum(roll)
        # Change position by mod 22 so that position resets upon passing all properties
        if self.position > 22:
            self.position %= 22
        # If double roll (dice show same value), roll again by calling this function (recursion)
        if roll[0] == roll[1]:
            self.move_token() 

    