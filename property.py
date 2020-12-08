
class Property:
    def __init__(self, name, color, rent):
        """Each property has a name, a color denoting its group, and a base rent value."""
        self.name = name
        self.color = color
        self.rent = rent
        self.price = rent * 5 #Cost of buying an unoccupied property from the bank (5 times initial rent)
        self.owned = False #Ownership status
        self.buildings = 0

    def buy_property(self):
        self.owned = True

    def sell_property(self):
        self.owned = False
    
    def update_rent(self, buy = True):
        if buy:
            self.rent *= 2
        else:
            self.rent /= 2
    
    # For the purposes of rent, a hotel is equivalent to 5 houses

    def add_building(self):
        self.buildings += 1
        self.update_rent()

    def remove_building(self):
        self.buildings -= 1
        self.update_rent(False)
