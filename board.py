from Property import Property

class Board:
    def __init__(self):
        """Define a list to hold Property objects. 
        Tokens proceed on the board by iterating through this list."""
        self.spaces = [] #List of properties
        self.spaces[0] = Property("Go!", "None", -200) #Assign the Go space to the first position

    def add_property(self, name, color, rent):
        """Add a property to the list of spaces by instantiaing a Property object."""
        self.spaces.append(Property(name, color, rent))

    def show_property(self, position):
        """Pass in a position index to see the property's name."""
        current_property = self.spaces[position]
        print(f"You landed on {current_property.name}!")
        return current_property
