name = 'inp.txt'
handle = open(name)
d = []
count = 0
c = []
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
            if len(d) == 7:
                for i in d:
                    c.append(i[0:3])
                check = all(item in c for item in list)
                if check is True:
                    count +=1
                c = []
        d = []
print(count)
