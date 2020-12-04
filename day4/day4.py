"""
usage: $ python day4.py <input-file>
"""

import sys
import string


class passport:
        def __init__(self,pp,fields):

            try:
                del pp['cid']
            except KeyError:
                pass

            self.byr = (1920 <= int(pp['byr']) <= 2002) and (len(pp['byr'])==4)
            self.iyr = (2010 <= int(pp['iyr']) <= 2020) and (len(pp['iyr']) ==4)
            self.eyr = (2020 <= int(pp['eyr']) <= 2030) and (len(pp['eyr']) ==4)
            self.hcl = (pp['hcl'][0] =='#') and (len(pp['hcl'][1:]) == 6) and ( all([j in [str(i) for i in range(10)] + list(string.ascii_lowercase)[:6] for j in pp['hcl'][1:]]) )
            self.ecl = pp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            self.pid = (len(pp['pid']) ==9) and all([dig.isdigit() for dig in pp['pid']])
            
            if (pp['hgt'][:-2].isdigit() == True) and ( (pp['hgt'][-2:] == 'cm') or (pp['hgt'][-2:] == 'in')  ):
                if (pp['hgt'][-2:] == 'cm') and (150 <= int(pp['hgt'][:-2]) <= 193):
                    
                    self.hgt = True
                    
                elif (pp['hgt'][-2:] == 'in') and (59 <= int(pp['hgt'][:-2]) <= 76):
                    
                    self.hgt = True
                else:
                    self.hgt = False
                    
            else:
                self.hgt = False
                                    
            if all([self.__dict__[key] for key in fields]):
                self.valid = True
            else:
                self.valid = False
                                    
                
                
                
passdata = []
pdata_temp = []
with open(sys.argv[1], 'r') as fp:

    for line in fp:
        pdata_temp.append(line.split())
        if line.split() ==[]:
            
            passdata.append({keyvals.split(':')[0]:keyvals.split(':')[1] for keyvals in [j for i in pdata_temp for j in i]})
            pdata_temp = []
            
    passdata.append({keyvals.split(':')[0]:keyvals.split(':')[1] for keyvals in [j for i in pdata_temp for j in i]})
        

pf = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

valid = 0
for i in range(len(passdata)):
    if all(item in passdata[i].keys() for item in pf):

        ptest = passport(passdata[i],pf)    # comment out for part 1
        if ptest.valid == True:             # comment out for part 1
            valid += 1

print('There are',str(valid),'passports')
