# A class for each player of the game

import random

class Player:
    def __init__(self, token):
        """Initialize a player with a token of their choosing. 
        Every player begins with $1500, 0 houses, and 0 hotels at the start of the game."""
        self.token = token
        self.balance = 1500
        self.houses = 0
        self.hotels = 0
    
    def roll_dice(self):
        # Roll two standard dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"{die1}, {die2}")
        if die1 == die2:
            print("Double roll!")

    def collect_rent(self, other, rent):
        # Pass in the other player's name and rent amount
        # Add rent amount to self and deduct rent amount from the other player
        self.balance += rent
        other.balance -= rent