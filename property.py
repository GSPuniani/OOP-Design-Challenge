
class Property:
    def __init__(self, name, color, rent):
        """Each property has a name, a color denoting its group, and a base rent value."""
        self.name = name
        self.color = color
        self.rent = rent
        self.owned = False #Ownership status
        self.buildings = 0

    def buy_property(self):
        self.owned = True

    def sell_property(self):
        self.owned = False
    
    def update_rent(self, buy = False):
        if buy:
            self.rent *= 2
        else:
            self.rent /= 2
    
    def add_building(self):
        self.buildings += 1
        self.update_rent(True)

    def remove_building(self):
        self.buildings -= 1
        self.update_rent()
