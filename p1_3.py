#!/usr/bin/env python

# http://cryptopals.com/sets/1/challenges/3/

import sys
import binascii
from p1_1 import *
from p1_2 import *

if __name__ == '__main__':
    stringa = binascii.unhexlify(sys.argv[1])
    sentences = []
    for c in range(256):
        stringb = chr(c) * len(stringa)
        sentences.append("".join([chr(ord(a)^ord(b)) for a, b in zip(stringa, stringb)]))
    matches = []
    with open('/usr/share/dict/words') as f:
        dictwords = map(str.strip, f.readlines())
    for s in sentences:
        nummatches = 0
        words = s.split()
        for w in words:
            if w in dictwords:
                nummatches += 1
        matches.append((nummatches, s))
    print max(matches)[1]

