lines = ''
with open('./input.txt') as f:
    lines = f.readlines()

numbers = '0123456789'
result = 0
for line in lines:
    num = '0'
    for char in line:
        if char in numbers:
            num += char
            break
    i = len(line) -1
    while i >= 0:
        if line[i] in numbers:
            num += line[i]
            break
        i -= 1
    result += int(num)
print(result)