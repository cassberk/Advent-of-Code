"""
usage: $ python day7.py <input-file>
"""

import sys
from functools import reduce
import re

def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start].items():
        if node[0] not in path:
            
            newpath = find_path(graph, node[0], end, path)
            
            if newpath:
                return newpath
    return None


def bagcheck(rule):
    return (rule !='bag') and (rule !='bags') 


def count_bags(bag,start_cnt):

    accumulated_bags = start_cnt

    for sub_bag,num in graph[bag].items():

        for k in range(num):
            accumulated_bags+=1
            accumulated_bags = count_bags(sub_bag,accumulated_bags)

    return accumulated_bags
        
    
rulelist = []
f = open(sys.argv[1], 'r')

for lines in f.readlines():
    words = lines.split()
    rulelist.append(list(map(remove_punctuation, words)))

f.close()

    
graph = {}
for idx in range(len(rulelist)):
    concatlist = list(filter(bagcheck,rulelist[idx]))

    keyvals = ''.join(concatlist).split('contain')
    if 'other' in keyvals[1]:
        keyvals[1] = keyvals[1].replace('no','0')

    splitvals = ''.join(["!!" if char.isdigit() else char for char in keyvals[1]]).split('!!')

    ver = list(filter(None,splitvals))
    weights = [char for char in keyvals[1] if char.isdigit() ]

    ver_weights = {ver[i]:int(weights[i]) for i in range(len(ver))}

    graph[keyvals[0]] = ver_weights
    

bagcombo = 0
for key in graph.keys():
    if key != 'shinygold':
        
        path = find_path(graph,key,'shinygold')
        if path != None:
            bagcombo +=1

# Part 1
print('There are',bagcombo,'bagcombos')

# Part 2
starting_bag = 'shinygold'
total_bags = count_bags(starting_bag,0)

print('and',total_bags, 'in your',starting_bag,'bag')
