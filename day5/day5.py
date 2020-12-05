"""
usage: $ python day5.py <input-file>
"""

import sys

seatinfo = []
f = open(sys.argv[1], 'r')
for lines in f.readlines():
    seatinfo.append(lines.replace("\n",""))
f.close()

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

seatid = []
idmax = 0
for seat in enumerate(seatinfo):
    
    rowchunk = [item for item in range(128)]
    colchunk = [item for item in range(8)]
    
    for _ in range(len(seat[1])):
        if seat[1][_] == 'F':
            rowchunk = split_list(rowchunk)[0]
        elif seat[1][_] =='B':
            rowchunk = split_list(rowchunk)[1]

        elif seat[1][_] == 'L':
            colchunk = split_list(colchunk)[0]
        elif seat[1][_] =='R':
            colchunk = split_list(colchunk)[1]

    seatid.append(8*rowchunk[0] + colchunk[0])
    
    if seatid[seat[0]] >= idmax:
        idmax = seatid[seat[0]]
        
seatidsort =sorted(seatid)

print('max SeatId: ',idmax)

for i in range(len(seatidsort)-1):
    if (not seatidsort[i]+1 == seatidsort[i+1]):
        print('Your seat is: ',seatidsort[i]+1)
        
