# Advent of Code - P1
import math

with open('input1.dat', 'r') as massesFile:
    massesStr = massesFile.read().splitlines()
    massesFile.close()
    fuel = 0.0
    for massStr in massesStr:
        fuelTemp = math.floor(float(massStr) / 3) - 2
        if fuelTemp > 0:
            fuel += fuelTemp
    
    print(f'Total fuel required for all of the modules on my spacecraft is {fuel} liters.')

with open('input1.dat', 'r') as massesFile:
    massesStr = massesFile.read().splitlines()
    massesFile.close()
    fuel = 0.0
    for massStr in massesStr:
        fuelTemp = math.floor(float(massStr) / 3) - 2
        while fuelTemp > 0:
            fuel += fuelTemp
            fuelTemp = math.floor(fuelTemp / 3) - 2
    
    print(f'Total fuel required for all of the modules on my spacecraft is {fuel} liters (taking the mass of the added fuel into account).')

# Advent of Code - Day 2 Part 1

def addition(position1, position2, position3, numbers):
    numbers[position3] = numbers[position1] + numbers[position2]
    return numbers

def multiplication(position1, position2, position3, numbers):
    numbers[position3] = numbers[position1] * numbers[position2]
    return numbers

optCodeInstruction = {
    1 : addition,
    2 : multiplication
}

with open('input2.dat', 'r') as program:
    numbers = [int(number) for number in program.read().split(',')]
    numbers[1] = 12
    numbers[2] = 2
    program.close()

    optCodePosition = 0
    while optCodePosition < len(numbers):
        optCode = numbers[optCodePosition]
        if optCode != 99:
            position1 = numbers[optCodePosition + 1]
            position2 = numbers[optCodePosition + 2]
            position3 = numbers[optCodePosition + 3]
            numbers = optCodeInstruction[optCode](position1, position2, position3, numbers)
            optCodePosition += 4
        else:
            print(f'Program halted at position: {optCodePosition}')
            break
    
    print(f'Value left at position 0 after the program halts is: {numbers[0]}')

# Advent of Code - Day 1 Part 2

targetValue = 19690720

with open('input2.dat', 'r') as program:
    numbersIntact = [int(number) for number in program.read().split(',')]
    program.close()

    done = False
    for i in range(0,99):
        for j in range(0,99):
            numbers = numbersIntact.copy()
            numbers[1] = i
            numbers[2] = j
            optCodePosition = 0
            while optCodePosition < len(numbers):
                optCode = numbers[optCodePosition]
                if optCode != 99:
                    position1 = numbers[optCodePosition + 1]
                    position2 = numbers[optCodePosition + 2]
                    position3 = numbers[optCodePosition + 3]
                    numbers = optCodeInstruction[optCode](position1, position2, position3, numbers)
                    optCodePosition += 4
                else:
                    break
            if numbers[0] == targetValue:
                print(f'The noun and verb that create an output of 19690720 are {i} and {j}')
                done = True
                break
        else:
            continue
        break
    
    if done: 
        print(f'100 * noun + verb is: {100 * i + j}')
    else:
        print('Error - Cannot find the requested noun and verb!') 

# Advent of Code - Day 3 Part 1

def moveUp(point):
    point[1] += 1
    return point

def moveDown(point):
    point[1] -= 1
    return point

def moveLeft(point):
    point[0] -= 1
    return point

def moveRight(point):
    point[0] += 1
    return point

move = {
    'U' : moveUp,
    'D' : moveDown,
    'L' : moveLeft,
    'R' : moveRight
}

with open('input3.dat', 'r') as coordinatesObj:
    coordinatesWire1 = [coordinate1 for coordinate1 in coordinatesObj.readline().split(',')]
    coordinatesWire2 = [coordinate2 for coordinate2 in coordinatesObj.readline().split(',')]

visitedPoints1 = {}
visitedPoints2 = {}
intersections = {}

origin = [0, 0]
currentPoint = origin
step = 1
for coord in coordinatesWire1:
    direction = coord[:1]
    units = int(coord[1:])
    for i in range(0, units):
        visitedPoint = move[direction](currentPoint.copy())
        currentPoint = visitedPoint.copy()
        if (visitedPoint[0], visitedPoint[1]) not in visitedPoints1:
            visitedPoints1[(visitedPoint[0], visitedPoint[1])] = step
        step += 1
        
currentPoint = origin
step = 1
for coord in coordinatesWire2:
    direction = coord[:1]
    units = int(coord[1:])
    for i in range(0, units):
        visitedPoint = move[direction](currentPoint.copy())
        currentPoint = visitedPoint.copy()
        if (visitedPoint[0], visitedPoint[1]) not in visitedPoints2:
            visitedPoints2[(visitedPoint[0], visitedPoint[1])] = step
        step += 1

distances = []
steps = []
intersections = set(visitedPoints1.keys()).intersection(set(visitedPoints2.keys()))
for intersection in intersections:
    distances.append(abs(intersection[0]) + abs(intersection[1]))
    steps.append(visitedPoints1[intersection] + visitedPoints2[intersection])

print('The shortest distance is', min(distances))
print('The fewest number of combined steps is', min(steps))