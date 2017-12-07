#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    for x in range(1, len(sys.argv)):
        total += int(sys.argv[x])
    print(total)
