import re
lines = ''
with open('./input.txt') as f:
    lines = f.readlines()

def byIndex(elem):
    return elem[1]

log = ''

numbersString = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = '123456789'
result = 0
for line in lines:
    num = '0'
    pairs = []

    # Find all number occurences in line and save them along with index
    index = 1
    for number in numbersString:
        for m in re.finditer(number, line):
            pairs.append((index, m.start()))
        index += 1
    
    for number in numbers:
        for m in re.finditer(number, line):
            pairs.append((number, m.start()))
    
    pairs.sort(key=byIndex)

    if len(pairs) > 0:
        num += str(pairs[0][0])
    if len(pairs) == 1: # first and last number are same if only 1 number
        num += str(pairs[0][0])
    elif len(pairs) > 1:
        num += str(pairs[-1][0])
    
    result += int(num)

print(result)

with open("./logs.txt", 'w') as f:
    f.write(log)