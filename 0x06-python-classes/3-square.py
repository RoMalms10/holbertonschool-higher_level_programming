#!/usr/bin/python3
class Square:
    """Creates a square"""
    def __init__(self, size=0):
        """Initializes the size of a square

         Args:
            size (int): The size of the square
        """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
    def area(self):
        """Calculates the area of the square
            
        Returns: The value of the area
        """
        return self.__size**2
