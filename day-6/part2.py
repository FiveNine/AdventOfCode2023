import math
import timeit
import re

start = timeit.default_timer()

lines = ['','']

with open('input.txt') as f:
    currentLine = 0
    char = f.read(1)
    while char:
        if char.isdigit():
            lines[currentLine] += char
        elif not char.isspace() and len(lines[currentLine]) > 0:
            currentLine += 1
        char = f.read(1)

time = int(''.join(re.findall(r'\d+', lines[0])))
distance = int(''.join(re.findall(r'\d+', lines[1])))


timeButtonHeldDown_lower = math.ceil(time - math.sqrt(time**2 - 4*distance) / 2)
timeButtonHeldDown_upper = int(time + math.sqrt(time**2 - 4*distance) / 2)

print(timeButtonHeldDown_upper - timeButtonHeldDown_lower + 1)
print((timeit.default_timer()-start) * 1000, 'ms')
