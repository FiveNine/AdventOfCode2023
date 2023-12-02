lines = ''
with open('./input.txt') as f:
    lines = f.readlines()

result = 0
for line in lines:
    gameId, allSets = line.split(':')
    result += int(gameId)
    allSets = allSets.strip(' ').split(';')

    for set in allSets:
        r, g, b = 0, 0, 0
        for cube in set.split(','):
            cube = cube.strip(' ')
            if 'red' in cube:
                r += int(cube.split(' ')[0])
            elif 'green' in cube:
                g += int(cube.split(' ')[0])
            elif 'blue' in cube:
                b += int(cube.split(' ')[0])
        if (r > 12 or g > 13 or b > 14):
            result -= int(gameId)
            break

print(result)