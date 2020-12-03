import sys

import numpy as np

forest = []
with open(sys.argv[1], 'r') as fp:
    for line in fp:
        forest.append(line.replace("\n", ""))
fp.close()

slopelist = []
for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:

    
    tree_cnt = 0
    iter = slope[0]
    
    for i in range(1,len(forest),slope[1]):

        if forest[i][iter%len(forest[0])] =='#':

            tree_cnt +=1
            
        iter += slope[0]
    slopelist.append(tree_cnt)

print(slopelist)
print(np.prod(slopelist))
