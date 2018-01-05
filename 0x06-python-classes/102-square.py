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

    @property
    def size(self):
        """Getter - gets the size of the square
        Returns: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter - sets the value of the size of the square
        Args:
            value (int): the size of the square
        """
        if type(value) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square
        Returns: The value of the area
        """
        return self.__size**2

    def __lt__(self, other):
        """ Check if self size is less than other size
        """
        return self.size < other.size

    def __le__(self, other):
        """ Check if self size is less than or equal to other size
        """
        return self.size <= other.size

    def __eq__(self, other):
        """ Check if self size is equal to other size
        """
        return self.size == other.size

    def __ne__(self, other):
        """ Check if self size is not equal to other size
        """
        return self.size != other.size

    def __gt__(self, other):
        """ Check if self size is greater than other size
        """
        return self.size > other.size

    def __ge__(self, other):
        """ Check if self size is greater than or equal to other size
        """
        return self.size >= other.size
