name = input("Enter file:")
handle = open(name)
correct = 0

for lines in handle:
    r = lines.split()
    limit = r[0]
    limit = limit.split("-")
    low = int(limit[0])-1
    high = int(limit[1])-1
    letter = r[1]
    letter = letter[0]
    passcodes = r[2]
    if passcodes[low] is letter and passcodes[high] is letter:
        continue
    elif passcodes[low] is letter or passcodes[high] is letter:
        correct = correct+1
print(correct)
