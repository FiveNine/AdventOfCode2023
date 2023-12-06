import re

with open('input.txt') as f:
    lines = f.readlines()

times = re.findall(r'\d+', lines[0])
distances = re.findall(r'\d+', lines[1])

result = 1
for i, time in enumerate(times):
    wins = 0
    time = int(time)
    distance = int(distances[i])

    waitTimes = []
    for waitTime in range(time):
        timeLeft = time - waitTime
        speed = waitTime
        distanceTravelled = speed * timeLeft
        if distanceTravelled > int(distances[i]):
            wins += 1
            waitTimes.append(waitTime)
    result *= wins
print(result)