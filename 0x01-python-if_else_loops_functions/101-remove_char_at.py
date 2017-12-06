#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = str
    cpy = cpy[:n] + cpy[(n+1):]
    if n < 0:
        return str
    return cpy
