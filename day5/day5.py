name = input("Enter file:")
handle = open(name)
tot = []
for lines in handle:
    numb = 128
    num = 8
    count = 0
    c = 0
    for lett in lines:
        numb = numb/2
        if lett == 'B':
            count += numb
        if lett == 'R':
            num = num/2
            c += num
        if lett == 'L':
            num = num/2
    to = int(count * 8 + c)
    tot.append(to)
tot.sort()
print(max(tot))
def find_missing(tot): 
    return [x for x in range(tot[0], tot[-1]+1)  
                               if x not in tot] 
print(find_missing(tot)) 
