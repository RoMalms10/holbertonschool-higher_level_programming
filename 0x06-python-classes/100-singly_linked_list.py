#!/usr/bin/python3
class Node:
    """ Creates a new node
    """
    
    def __init__(self, data, next_node=None):
        """ Initializes the information in the node

        Args:
            data (int): The value to be stored in the node
            next_node (Node): The next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter - Retrieves the value for data

        Returns:
            the value held in data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter - Sets the value for data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getter - Retrieves the value for next_node

        Returns:
            the value held in next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter - sets the value for next_node
        """
        if value != None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ Creates a singly linked list
        And adds new nodes in a sorted fashion
    """

    def __init__(self):
        """Initializes head to nothing
        """
        self.__head = None

    def __str__(self):
        """prints the list when print is used on the class

        Returns:
            The string to be printed
        """
        new_str = ""
        pr = self.__head
        while pr != None:
            new_str += str(pr.data)
            pr = pr.next_node
            if pr != None:
                new_str += "\n"
        return new_str

    def sorted_insert(self, value):
        """Sorts the list
           Then: Inserts a new Node at the correct position

        Args:
            Value (int): The value to store in the new node
        """
        self.new_node = Node(value, None)
        temp = self.__head
        # Checks if there is no list
        if self.__head == None:
           self.__head = self.new_node
        # Checks if the first value is bigger than the new node value
        elif temp.data > value:
            self.new_node.next_node = self.__head
            self.__head = self.new_node
        # Goes through the list to see where to add the new node
        else:
            while temp.next_node != None:
                if temp.next_node.data > value:
                    break
                temp = temp.next_node
            self.new_node.next_node = temp.next_node
            temp.next_node = self.new_node
