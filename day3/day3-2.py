name = input("Enter file:")
spot = 0
tree = 0
end = []
forest = [1,3,5,7]
for t in forest:
    handle = open(name)
    for lines in handle:
        l = len(lines)-1
        if lines[spot] == '#':
            tree += 1
        spot = spot+t
        if spot >= l:
            spot = spot -l
        #print(spot)
    end.append(tree)
    spot = 0
    tree=0

handle = open(name)
line=0
for lines in handle:
    if line == 1:
        line = line -1
        continue
    l = len(lines)-1
    if lines[spot] == '#':
        tree += 1
    spot = spot+1
    if spot >= l:
        spot = spot -l
    line += 1
end.append(tree)
print(end)

res = 1
for x in end:
    res = res*x
print(res)
