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

def GetLeftDigits(row, numberIndex):
    digits = ''
    endIndex = numberIndex[1]
    if endIndex > 0:
        for char in row[:endIndex]:
            if char.isdigit():
                digits += char
            else:
                digits = ''
    return digits

def GetNumbersAround(array, startCoords):
    coordsToSearch = []
    i, j = startCoords
    coordsToSearch.append((i, j - 1)) # left
    coordsToSearch.append((i, j + 1)) # right
    coordsToSearch.append((i - 1, j)) # top
    coordsToSearch.append((i + 1, j)) # down
    coordsToSearch.append((i - 1, j - 1)) # top-left
    coordsToSearch.append((i - 1, j + 1)) # top-right
    coordsToSearch.append((i + 1, j - 1)) # down-left
    coordsToSearch.append((i + 1, j + 1)) # down-right

    coordsSearched = []
    numbersFound = []
    for coord in coordsToSearch:
        # if len(coordsSearched) > 0:
        #     print(f"Coords searched: {coordsSearched}")
        if coord not in coordsSearched:
            if coord[0] < len(array) and coord[0] >= 0: # bounds check
                if coord[1] < len(array[coord[0]]) and coord[1] >= 0: # bounds check
                    if array[coord[0]][coord[1]].isdigit():
                        leftDigits = GetLeftDigits(array[coord[0]], (coord[0], coord[1]))
                        rightDigits = GetRightDigits(array[coord[0]], (coord[0], coord[1]))
                        
                        # Save number's coordinates so it doesnt search them again
                        rangeStart = coord[1] - len(leftDigits)
                        rangeEnd = coord[1] + len(rightDigits)+1
                        for index in range(rangeStart, rangeEnd):
                            coordsSearched.append((coord[0], index))
                        
                        num = leftDigits + array[coord[0]][coord[1]] + rightDigits
                        # print(f"Searching: {array[coord[0]][coord[1]]} found {num} range: ({rangeStart}, {rangeEnd})")
                        numbersFound.append(num)
    return numbersFound


result = 0
i = 0
while i < len(engine):
    j = 0
    while j < len(engine[i]):
        if engine[i][j] == '*':
            numbers = GetNumbersAround(engine, (i, j))
            print(numbers, i, j)
            if len(numbers) == 2:
                result += int(numbers[0]) * int(numbers[1])
        j += 1
    i += 1

print(result)

