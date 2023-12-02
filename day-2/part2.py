lines = ''
with open('./input.txt') as f:
    lines = f.readlines()

result = 0
for line in lines:
    gameId, allSets = line.split(':')
    allSets = allSets.strip(' ').split(';')

    r, g, b = 0, 0, 0
    for set in allSets:
        for cube in set.split(','):
            cube = cube.strip(' ')
            if 'red' in cube:
                num = int(cube.split(' ')[0])
                if num > r:
                    r = num
            elif 'green' in cube:
                num = int(cube.split(' ')[0])
                if num > g:
                    g = num
            elif 'blue' in cube:
                num = int(cube.split(' ')[0])
                if num > b:
                    b = num
    result += r*g*b

print(result)