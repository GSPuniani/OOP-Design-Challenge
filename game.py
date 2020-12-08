# Run this file to simulate gameplay

from player import Player
from bank import Bank
from board import Board

# Instantiate board and add all of the properties
monopoly = Board()
monopoly.add_property("Mediterranean Avenue", "Purple", 60)
monopoly.add_property("Baltic Avenue", "Purple", 60)
monopoly.add_property("Oriental Avenue", "Light Blue", 100)
monopoly.add_property("Vermont Avenue", "Light Blue", 100)
monopoly.add_property("Connecticut Avenue", "Light Blue", 120)
monopoly.add_property("St. Charles Place", "Violet", 140)
monopoly.add_property("States Avenue", "Violet", 140)
monopoly.add_property("Virginia Avenue", "Violet", 160)
monopoly.add_property("St. James Place", "Orange", 180)
monopoly.add_property("Tennessee Avenue", "Orange", 180)
monopoly.add_property("New York Avenue", "Orange", 200)
monopoly.add_property("Kentucky Avenue", "Red", 220)
monopoly.add_property("Indiana Avenue", "Red", 220)
monopoly.add_property("Illinois Avenue", "Red", 240)
monopoly.add_property("Atlantic Avenue", "Yellow", 260)
monopoly.add_property("Ventnor Avenue", "Yellow", 260)
monopoly.add_property("Marvin Gardens", "Yellow", 280)
monopoly.add_property("Pacific Avenue", "Green", 300)
monopoly.add_property("North Carolina Avenue", "Green", 300)
monopoly.add_property("Pennsylvania Avenue", "Green", 320)
monopoly.add_property("Park Place", "Dark Blue", 350)
monopoly.add_property("Boardwalk", "Dark Blue", 400)



# Instantiate players
joi = Player("Race Car")
gobind = Player("Battleship")

print(f"Initial balances of all players: ${joi.balance}, ${gobind.balance}")

# Instantiate bank
bank = Bank()

print("\nJoi:")
joi.move_token()
monopoly.show_property(joi.position)
print(joi.position)

print("\nGobind:")
gobind.move_token()
# Buy the property
gobind_purchase1 = monopoly.show_property(gobind.position)
# Check if anyone owns it first
if gobind_purchase1.owned == False:
    gobind_purchase1.buy_property(gobind)
gobind.pay(bank, gobind_purchase1.price)
print(gobind.position)
print("Gobind's properties:")
for prop in gobind.properties:
    print(prop.name)

print(f"Joi's balance: {joi.balance}")
print(f"Gobind's balance: {gobind.balance}")

# Put a house on the property
bank.sell_building(gobind)
gobind_purchase1.add_building()
print(f"Gobind's balance: {gobind.balance}")
# Collect rent from Joi
gobind.collect(joi, gobind_purchase1.rent)

print(f"Joi's balance: {joi.balance}")
print(f"Gobind's balance: {gobind.balance}")


print("\nJoi:")
joi.move_token()
monopoly.show_property(joi.position)
print(joi.position)

print("\nGobind:")
gobind.move_token()
monopoly.show_property(gobind.position)
print(gobind.position)

print("\nJoi:")
joi.move_token()
monopoly.show_property(joi.position)
print(joi.position)

print("\nGobind:")
gobind.move_token()
monopoly.show_property(gobind.position)
print(gobind.position)

print("\nJoi:")
joi.move_token()
monopoly.show_property(joi.position)
print(joi.position)

print("\nGobind:")
gobind.move_token()
monopoly.show_property(gobind.position)
print(gobind.position)

# Pass Go and collect $200 from the bank
joi.collect(bank, 200)
print(f"Joi's balance: {joi.balance}")
gobind.collect(bank, 200)
print(f"Gobind's balance: {gobind.balance}")

print("\nJoi:")
joi.move_token()
monopoly.show_property(joi.position)
print(joi.position)

print("\nGobind:")
gobind.move_token()
monopoly.show_property(gobind.position)
print(gobind.position)


