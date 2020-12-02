# day 2-1: find how many passwords are correct

name = input("Enter file:")
handle = open(name)
counts = 0
correct = 0
for lines in handle:
    r = lines.split()
    limit = r[0]
    limit = limit.split("-")
    low = int(limit[0])
    high = int(limit[1])
    letter = r[1]
    letter = letter[0]
    passcodes = r[2]
    for d in passcodes:
        if d is letter:
            counts = counts+1
    if counts <= high and counts >= low:
        correct = correct+1
    counts = 0
    print(correct)
