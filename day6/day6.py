"""
usage: $ python day6.py <input-file>
"""

import sys

planelist = []
grouplist = []
f = open(sys.argv[1], 'r')
for lines in f.readlines():
    if lines != "\n":
        grouplist.append(lines.replace("\n",""))
    elif lines == "\n":
        planelist.append(grouplist)
        grouplist = []
planelist.append(grouplist)
f.close()

cnt0 = 0
cnt1 = 0

for group in planelist:
    
    cnt0 += len(list(dict.fromkeys(''.join(group))))
    
    Uyes = list(set.intersection(*map(set, group)))
    
    if Uyes != []:
        cnt1 += len(Uyes)
        
        
print('# of yes questions: ',cnt0)
print('# of common yes questions: ',cnt1)