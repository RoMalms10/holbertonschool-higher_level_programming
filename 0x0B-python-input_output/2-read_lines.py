#!/usr/bin/python3
""" My module for reading files
"""


def read_lines(filename="", nb_lines=0):
    """ Reads a certain amount of lines from a file

    Args:
        filename (str): the file to read
        nb_lines (int): the numer of line to read
    """
    linecount = 0
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            linecount += 1

        # reset to the beginning of the file
        f.seek(0)

        if 0 < nb_lines < linecount:
            for line in f:
                if (nb_lines == 0):
                    break
                print(line, end="")
                nb_lines -= 1
        else:
            for line in f:
                print(line, end="")
