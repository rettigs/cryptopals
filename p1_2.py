#!/usr/bin/env python

# http://cryptopals.com/sets/1/challenges/2/

def hex_xor(a, b):
    '''Given two hex strings, bitwise XORs them and returns the result.'''
    #return operator.xor(*map(int, sys.argv[1:3], [16]*2))
    a, b = map(int, sys.argv[1:3], [16]*2)
    return "{:x}".format(a ^ b)

if __name__ == '__main__':
    import sys
    print hex_xor(*sys.argv[1:3])
