# Run this file to simulate gameplay

from player import Player
from bank import Bank
from board import Board

# Instantiate board
monopoly = Board()
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)
monopoly.add_property("New York Avenue", "red", 200)


# Establish players
joi = Player("Car")
gobind = Player("Hat")

# Instantiate bank
bank = Bank()

joi.move_token()
monopoly.show_property(joi.position)
print(joi.position)