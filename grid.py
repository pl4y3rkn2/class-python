from functools import reduce
import random
from array import Array
"""
Code used for the 'Crear un array de dos dimensiones' class.

Grid type class
Methods:
    1. Initialize
    2. Get height
    3. Get width
    4. Access item
    5. String representation
"""



class Grid(object):
    """Represents a two-dimensional array."""
    def __init__(self, rows, columns, fill_value = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        "Returns the number of rows."
        return len(self.data)

    def get_width(self):
        """Returns the number of columns."""
        return len(self.data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][column]."""
        return self.data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)

'''
Code used in the shell to instance a grid



print(matrix)
matrix.get_height()
matrix.get_width()
matrix.__getitem__()
matrix.__getitem__(1)
matrix.__getitem__(2)[0]
matrix.__str__()
'''
matrix = Grid(3, 3)
print(matrix)
for row in range(matrix.get_height()):
    for column in range(matrix.get_width()):
        matrix[row][column] = [random.randint(0, 100) for i in range(3)]

print(matrix)