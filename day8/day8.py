"""
usage: $ python day7.py <input-file>
"""

import sys


rulelist = []
f = open(sys.argv[1], 'r')

code = [cmd.replace('\n','').split() for cmd in f.readlines()]
f.close()


def switch_str(argument): 
    switcher = { 
        'jmp': 'nop', 
        'nop': 'jmp', 
    } 
    return switcher.get(argument, None) 

# part 1
def jumparound():
    it = 0
    count = 0
    itlist = []
    go =True
    while go == True:

        try:

            if it in itlist:

                go =False
                break
            else:
                itlist.append(it)

            if code[it][0] == 'acc':
                count += int(code[it][1])
                it += 1
            elif code[it][0] == 'jmp':
                it += int(code[it][1])
            else:
                it += 1
        except:
            return count
        
    return count

print('The answer topart 1 is',jumparound())

# part 2
for k in enumerate(code):
    
    if switch_str(k[1][0]) is not None:
        
        code[k[0]][0] = switch_str(k[1][0])
    
    
        it = 0
        count = 0
        itlist = []
        go =True
        while go == True:

            try:
                if it in itlist:

                    code[k[0]][0] = switch_str(code[k[0]][0])
                    go =False
                    break
                else:
                    itlist.append(it)

                if code[it][0] == 'acc':
                    count += int(code[it][1])
                    it += 1
                elif code[it][0] == 'jmp':
                    it += int(code[it][1])
                else:
                    it += 1
            
            except:
                print('The answer to part 2 is',count)



