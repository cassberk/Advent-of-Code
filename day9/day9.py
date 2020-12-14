"""
usage: $ python day9.py <input-file>
"""

import sys
import itertools
import numpy as np

f = open(sys.argv[1],"r")

xmas = [int(cmd.replace('\n','')) for cmd in f.readlines()]
f.close()

for i in range(25,len(xmas)):

    sequence = xmas[i-25:i]

    if xmas[i] not in [sum(j) for j in itertools.combinations(sequence, 2)]:
        key = xmas[i]
        print('Part 1: The first number is',key)

for i in range(len(xmas)):
    if key in itertools.accumulate(xmas[i:]):
        break
        
seqlen = list(itertools.accumulate(xmas[i:])).index(key) + 1

seq = xmas[i:seqlen+i]
# print(seq)
print('Part 2: The encryption weakness is ',np.min(seq)+np.max(seq))

