engine = []
with open('./input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line[0: -1] # remove \n character
        engine.append([*line])



def GetRightDigits(row, numberIndex):
    digits = ''
    startIndex = numberIndex[1]+1
    if startIndex < len(row):
        for char in row[startIndex:]:
            if char.isdigit():
                digits += char
            else:
                break
    return digits

def IsSpecialCharacterAround(array, number, startCoords):
    coordsToSearch = []
    i, j = startCoords
    coordsToSearch.append((i, j - 1)) # left
    coordsToSearch.append((i, j + len(number))) # right
    coordsToSearch.append((i - 1, j - 1)) # top-left
    coordsToSearch.append((i - 1, j + len(number))) # top-right
    coordsToSearch.append((i + 1, j - 1)) # down-left
    coordsToSearch.append((i + 1, j + len(number))) # down-right
    for a in range(len(number)):
        coordsToSearch.append((i - 1, j + a))
        coordsToSearch.append((i + 1, j + a))
    for coord in coordsToSearch:
        if coord[0] < len(array) and coord[0] >= 0: # bounds check
            if coord[1] < len(array[coord[0]]) and coord[1] >= 0: # bounds check
                if array[coord[0]][coord[1]] != '.':
                    if not array[coord[0]][coord[1]].isalnum():
                        return True
    return False


result = 0
i = 0
while i < len(engine):
    j = 0
    while j < len(engine[i]):
        msg = ''
        if engine[i][j].isdigit():
            rightDigits = GetRightDigits(engine[i], (i, j))
            num = engine[i][j] + rightDigits
            msg += f"{num} -> "
            if IsSpecialCharacterAround(engine, num, (i, j)):
                msg += f'Special found'
                result += int(num)
            else:
                msg += f"No special found"
            print(msg)
            j += len(num)-1
        j += 1
    i += 1

print(result)

