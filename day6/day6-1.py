name = 'inp.txt'
handle = open(name)
#list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'u','v','w','x','y','z']
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