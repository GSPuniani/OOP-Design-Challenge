from Property import Property

class Board:
    def __init__(self):
        """Define a list to hold Property objects. 
        Tokens proceed on the board by iterating through this list."""
        self.spaces = [Property("Go!", "None", -200)] #Assign the Go space to the first position
        self.count = 1 #Simple counter to keep track of the spaces on the board, starting with Go!

    def add_property(self, name, color, rent):
        """Add a property to the list of spaces by instantiating a Property object."""
        self.spaces.append(Property(name, color, rent))
        self.count += 1

    def show_property(self, position):
        """Pass in a position index to see the property's name."""
        current_property = self.spaces[position]
        print(f"You landed on {current_property.name}!")
        return current_property
