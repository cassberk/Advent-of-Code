f = open("/Volumes/GoogleDrive/My Drive/_Advent/day2/day2data.txt", "r")
pws = f.readlines()
f.close()

count = 0
for i in range(len(pws)):
    p1 = int(pws[i].split()[0].split('-')[0])
    p2 = int(pws[i].split()[0].split('-')[1])
    let = pws[i].split()[1][0]
    pw = pws[i].split()[2]
    
    if ((pw[p1-1] == let) or (pw[p2-1] == let)) and not ((pw[p1-1] == let) and (pw[p2-1] == let)) :
        count+=1
        
print('there are ',count,' valid passwords')
