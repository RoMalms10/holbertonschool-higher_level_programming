#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    for things in dir(hidden_4):
        if things[0] != "_":
            print(things)
