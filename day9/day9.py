name = 'inp.txt'
handle = open(name)
myList = []

for line in handle:
    line = int(line)
    myList.append(line)

twfive = []
j=0
find = 0
numb = 0
for i in range(len(myList)):
    if j == 25:
        j = 0
    if i <= 24:
        twfive.append(i)
    twfive[j] = myList[i]
    #print(twfive)
    if i > 24:
        b = 0
        for k in range(len(twfive)):
            find = myList[i+1] - twfive[k]
            b+=1
            if find == twfive[k]:
                continue
            if find in twfive:
                #print('found',myList[i+1], '=',  find, '+', twfive[k])
                break
        if b == 25:
            numb = myList[i+1]
            break
    j+=1
print(numb)
done = False
totlist = []
d=0
c =0
f = 0
while done == False:
    while d < len(myList):
        if c < numb:
            c += myList[d]
            d+=1
        if c > numb:
            c -= myList[f]
            f +=1
        if c == numb:
            print('done')
            print(f,d)
            done = True
            break
        i+=1
totlist = myList[f:d]
totlist.sort()
print(totlist[0] + totlist[-1])
