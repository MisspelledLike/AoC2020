name = input("Enter file:")
handle = open(name)
spot = 0
tree = 0

for lines in handle:
    l = len(lines)-1
    if lines[spot] == '#':
        tree += 1
    spot = spot+3
    if spot >= l:
        spot = spot -l
    print(spot)
print(tree)
