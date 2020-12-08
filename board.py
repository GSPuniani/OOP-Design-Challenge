from Property import Property

class Board:
    def __init__(self):
        self.spaces = []

    def add_property(self, name, color, rent):
        self.spaces.append(Property(name, color, rent))

    def show_property(self, position):
        current_property = self.spaces[position]
        print(f"You landed on {current_property.name}!")
        return current_property
