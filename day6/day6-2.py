name = 'inp.txt'
handle = open(name)
counts = dict()
row = 0
count = 0
lst = []
for line in handle:
    if line != '\n':
        row += 1
        for lett in line:
            if lett != '\n':
                counts[lett] = counts.get(lett, 0) + 1
    else:
        c = list(counts.values())
        for items in c:
            if items == row:
                count +=1
        lst.append(count)
        
        counts = dict()
        row = 0
        count = 0
    
print(sum(lst))
