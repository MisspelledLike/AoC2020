name = 'inp.txt'
handle = open(name)
check = []
count = 0
tot = []
for line in handle:
    if line != '\n':
        for lett in line:
            if lett not in check and lett is not '\n':
                check.append(lett)
                count += 1
    else:
        print(check, count)
        tot.append(count)
        check = []
        count = 0
    
print(sum(tot))
