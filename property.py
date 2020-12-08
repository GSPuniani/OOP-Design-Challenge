class Property:
    def __init__(self, name, color, rent):
        """Each property has a name, a color denoting its group, and a base rent value."""
        self.name = name
        self.color = color
        self.rent = rent
        self.price = rent * 5 #Cost of buying an unoccupied property from the bank (5 times initial rent)
        self.owned = False #Ownership status
        self.buildings = 0

    def buy_property(self, player):
        """Change ownership status to True when buying property."""
        self.owned = True
        # Add the property to the buying player's list of properties
        player.properties.append(self)

    def sell_property(self, player):
        """Change ownership status to False when selling property."""
        self.owned = False
        # Remove the property from the buying player's list of properties
        player.properties.remove(self)
    
    def update_rent(self, buy = True):
        """Double the rent if adding a building, otherwise halve the rent if removing."""
        if buy:
            self.rent *= 2
        else:
            self.rent /= 2
    
    # For the purposes of rent, a hotel is equivalent to 5 houses

    def add_building(self):
        """Increment the building count and double the rent."""
        self.buildings += 1
        self.update_rent()

    def remove_building(self):
        """Decrement the building count and halve the rent."""
        self.buildings -= 1
        self.update_rent(False)
