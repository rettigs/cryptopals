#!/usr/bin/env python

# http://cryptopals.com/sets/1/challenges/1/

def _int_to_bits(i,n): 
    '''Given an integer, returns it in binary form with the given number of digits.'''
    return [('0','1')[i>>j & 1] for j in xrange(n-1,-1,-1)]

def hex_to_base64(h):
    '''Given a hex string, returns it as a base64 string (using + and / as the last 2 characters).'''
    bits = "".join(["".join(_int_to_bits(int(c, 16), 4)) for c in h])
    bits += "0"*(len(bits)%6)
    base64 = ""
    while len(bits) > 0:
        index = int(bits[:6], 2)
        bits = bits[6:]
        if index <= 25:
            char = chr(index + 65)
        elif 26 <= index and index <= 51:
            char = chr((index - 26 + 97))
        elif 52 <= index and index <= 61:
            char = chr(index - 52 + 48)
        elif index == 62:
            char = '+'
        elif index == 63:
            char = '/'
        base64 += char

    return base64

if __name__ == '__main__':
    import sys
    print hex_to_base64(sys.argv[1])
