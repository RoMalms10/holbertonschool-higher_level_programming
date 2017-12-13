#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_sent = (len(sentence),
                  sentence[0] if sentence else "None")
    return tuple_sent
