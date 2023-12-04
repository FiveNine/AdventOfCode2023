import re
lines = []
with open('./input.txt') as f:
    lines = f.readlines()

result = 0
for line in lines:
    l, r = line.split(' | ')
    game, winningNumbers = l.split(': ')
    game = game[-1]

    winningNumbers = re.findall(r'\d+', winningNumbers)
    
    rolledNumbers = re.finditer(r'\d+', r)
    
    count = 0

    for num in rolledNumbers:
        print(num.group())
        if num.group() in winningNumbers:
            count += 1
    
    final = 0
    for i in range(count):
        if i == 0:
            final = 1
        else:
            final = final * 2
        print(final)
    result += final

print(result)