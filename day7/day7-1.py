name = 'inp.txt'
bags = [['shiny', 'gold']]

def calc(bags):
    for items in bags:
        handle = open(name)
        for lines in handle:
            x = lines.split()
            for i in range(len(x)-1):
                if x[i] == items[0] and x[i+1] == items[1]:
                    if x[0] != items[0] or x[1] != items[1]:
                        bags.append(x[:2])
    return bags
calc(bags)

tot = []
for i in bags:
    if i not in tot:
        tot.append(i)
print(len(tot)-1) #want 'shiny','gold' moet niet worden meegeteld
