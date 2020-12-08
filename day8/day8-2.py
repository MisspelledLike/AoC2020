name = 'inp.txt'
handle = open(name)
code = []
#while smthng == False:
for line in handle:
    line = line.split()
    code.append(line)

def jmpaccnop(tempcode):
    i = 0
    accumulator = 0
    lst1 = {}
    while i < len(tempcode):
        lst1[i] = lst1.get(i, 0) + 1
        if lst1[i] == 2:
            print('endless',accumulator)
            return 0
        if tempcode[i][0] == 'acc':
            accumulator += int(tempcode[i][1])
            i += 1
        elif tempcode[i][0] == 'jmp':
            i += int(tempcode[i][1])
        elif tempcode[i][0] == 'nop':
            i += 1
    print(accumulator)
    return accumulator

jmpaccnop(code)

for j in range(len(code)):
    trying = code.copy()
    if code[j][0] == 'nop':
        trying[j][0] = 'jmp'
        if jmpaccnop(trying) != 0:
            print('we winnnnn')
            break
        trying[j][0] = 'nop'
    elif code[j][0] == 'jmp':
        trying[j][0] = 'nop'
        if jmpaccnop(trying) != 0:
            print('we winnnnn')
            break
        trying[j][0] = 'jmp'
