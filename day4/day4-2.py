name = 'inp.txt'
handle = open(name)
d = []
count = 0
c = []
f = []
list = ['byr','iyr', 'eyr', 'hgt','hcl','ecl','pid']
for line in handle:
    if line != '\n':
        if not d:
            d = line.split()
        else:
            e = line.split()
            d = d + e
            e = []
    else:
        if len(d) >= 7:
            if len(d) ==8:
                count += 1
                f.append(d)
            if len(d) == 7:
                for i in d:
                    c.append(i[0:3])
                check = all(item in c for item in list)
                if check is True:
                    count +=1
                    f.append(d)
                c = []
        d = []
check = True
lists = ['a', 'b', 'c', 'd', 'e', 'f']
counts = 0
j =0
for lines in f:
    res = [tuple(map(str, sub.split(':'))) for sub in lines]
    res = dict(res)
    byr = int(res.get('byr'))
    if byr in range(1920, 2003):
        iyr = int(res.get('iyr')) 
        if iyr in range(2010,2021):
            eyr = int(res.get('eyr'))
            if eyr in range(2020,2031):
                hgt = res.get('hgt')
                if hgt[3:5] == 'cm' or hgt[2:4] == 'in':
                    if len(hgt) == 5:
                        hgt = int(hgt[0:3])
                    elif len(hgt) == 4:
                        hgt = int(hgt[0:2])
                    if hgt in range(150,194) or range(59,77):
                        hcl = res.get('hcl')
                        if hcl[0] == '#' and len(hcl) == 7:
                            hcl = hcl[1:]
                            for x in hcl:
                                if x in lists or range(0,10):
                                    j += 1
                            if j == 6:
                                j = 0
                                ecl = res.get('ecl')
                                if ecl in ['amb','blu','brn','gry','grn','hzl','oth']:
                                    pid = res.get('pid')
                                    if len(pid) == 9 and pid.isdigit() == True:
                                        counts += 1
                            else:
                                j = 0
print(counts)
