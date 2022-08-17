from functools import reduce
import random
"""
Code used for the 'Crear un array' class.

Array type class
Methods:
    1. Length
    2. String representation
    3. Membership
    4. Index.
    5. Replacement
"""

class Array(object):
    "Represents an array."

    def __init__(self, capacity, fill_value = None):
        """
        Args:
            capacity (int): static size of the array.
            fill_value (any, optional): value at each position. Defaults to None.
        """
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        """Returns capacity of the array."""
        return len(self.items)

    def __str__(self):
        """Returns string representation of the array"""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscrit operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, new_item):
        """Subscript operator for replacement at index."""
        self.items[index] = new_item

    def __sum__(self):
        return reduce(lambda a, b:
        a + b, self.items)

menu = Array(5)
for i in range(len(menu)):
    menu[i] = [random.randint(0, 100) for i in range(len(menu))]
    #print(menu[i])    

for i in range(len(menu)):
   print(menu[i]+menu[i])

print(menu.__sum__())