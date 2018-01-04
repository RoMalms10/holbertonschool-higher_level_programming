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

    def my_print(self):
        """Prints out the square with #'s"""
        if self.__size != 0:
            for index in range(self.__size):
                print("#"*self.__size)
        print()
