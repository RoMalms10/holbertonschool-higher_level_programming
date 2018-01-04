#!/usr/bin/python3
class Square:
    """Creates a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size of a square
         Args:
            size (int): The size of the square
            position (tuple(int, int)):
                tuple 1: how many spaces to print before the square
                tuple 2: how many new lines to print before the square
        """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        elif type(position[0]) != int or type(position[1]) != int:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        elif position[0] < 0 or position[1] < 0:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """Getter - gets the position

        Returns: the value of the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter - sets the value of the position
        Args:
            value (int): the position of the square
        """
        if type(self.__position[0]) != int or type(self.__position[1]) != int:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        elif self.__position[0] < 0 or self.__position[1] < 0:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square
        Returns: The value of the area
        """
        return self.__size**2

    def my_print(self):
        """Prints out the square with #'s"""
        if self.__size != 0:
            for new_line in range(self.__position[1]):
                print()
            for index in range(self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
        else:
            print()
