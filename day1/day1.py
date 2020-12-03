f = open("/Volumes/GoogleDrive/My Drive/_Advent/day1/data.txt", "r")
mula = f.readlines()
f.close()

x = [int(mula[_].split()[0]) for _ in range(len(mula))]



for i in range(len(x)):
    for j in range(len(x)):
        for k in range(len(x)):
            if x[i] + x[j] + x[k] == 2020:
                i_ = i
                j_ = j
                k_ = k
            # print(x[i],x[j])
#             break
#     break
print('The numbers are: ',x[i_],x[j_],x[k_])     

print('answer: ',str(x[i_]*x[j_]*x[k_]))