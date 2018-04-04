#!/usr/bin/python3
"""
"""


def find_peak(list_of_integers):
    """
    """
    if list_of_integers:
        beg = 0
        end = len(list_of_integers) - 1
        hold_beg = list_of_integers[beg]
        hold_end = list_of_integers[end]
        while beg < end and beg != end:
            if list_of_integers[beg] > hold_beg:
                hold_beg = list_of_integers[beg]
            if list_of_integers[end] > hold_end:
                hold_end = list_of_integers[end]
            beg = beg + 1
            end = end - 1
        if hold_beg > hold_end:
            return hold_beg
        else:
            return hold_end
