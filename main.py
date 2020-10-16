# Advent of Code - Day 1 Part 1

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

# Advent of Code - Day 1 Part 2

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

opCodeInstruction = {
    1 : addition,
    2 : multiplication
}

with open('input2.dat', 'r') as program:
    numbers = [int(number) for number in program.read().split(',')]
    numbers[1] = 12
    numbers[2] = 2
    program.close()

opCodePosition = 0
while opCodePosition < len(numbers):
    opCode = numbers[opCodePosition]
    if opCode != 99:
        position1 = numbers[opCodePosition + 1]
        position2 = numbers[opCodePosition + 2]
        position3 = numbers[opCodePosition + 3]
        numbers = opCodeInstruction[opCode](position1, position2, position3, numbers)
        opCodePosition += 4
    else:
        print(f'Program halted at position: {opCodePosition}')
        break

print(f'Value left at position 0 after the program halts is: {numbers[0]}')

# Advent of Code - Day 2 Part 2

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
        opCodePosition = 0
        while opCodePosition < len(numbers):
            opCode = numbers[opCodePosition]
            if opCode != 99:
                position1 = numbers[opCodePosition + 1]
                position2 = numbers[opCodePosition + 2]
                position3 = numbers[opCodePosition + 3]
                numbers = opCodeInstruction[opCode](position1, position2, position3, numbers)
                opCodePosition += 4
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

# Advent of Code - Day 3 Part 1 and 2

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

# Advent of Code - Day 4 Part 1 and 2

from collections import defaultdict

def rulesCheck(number):
    numberStr = str(number)
    repeats = defaultdict(int)
    isIncreasing = True
    for i in range(1, len(numberStr)):
        if (numberStr[i]) == (numberStr[i-1]):
            repeats[numberStr[i]] += 1 
        if (numberStr[i]) < (numberStr[i-1]):
            isIncreasing = False
            break
    
    return isIncreasing, repeats

lowerBound = 353096
upperBound = 843212
countPart1 = 0
countPart2 = 0
for number in range(lowerBound, upperBound):
    isIncreasing, repeats = rulesCheck(number)
    if isIncreasing and len(repeats) > 0:
        countPart1 +=1

    if isIncreasing and any(repeat == 1 for repeat in repeats.values()) :
        countPart2 +=1

print(countPart1, "numbers satisfy the rules in part 1!")
print(countPart2, "numbers satisfy the rules in part 2!")

# Advent of Code - Day 5 Part 1 and 2

def setAtPosition(inputValue, position, numbers):
    numbers[position] = inputValue
    return numbers

def outputAtPosition(inputValue, position, numbers):
    return numbers[position]

def getParameterPosition(opCodePosition, modePar, parameterNumber, numbers):
    return numbers[opCodePosition + parameterNumber] if modePar == 0 else opCodePosition + parameterNumber

with open('input5.dat', 'r') as program:
    numbers = [int(number) for number in program.read().split(',')]
    inputValue = 5 # part 1: 1, part 2: 5
    program.close()

outputs = []
diagnosticCode = 0
opCodePosition = 0
while opCodePosition < len(numbers):
    instructionCode = str(numbers[opCodePosition])
    nInstructionDigits = len(instructionCode)
    if nInstructionDigits < 3:
        opCode = int(instructionCode[-2:])
        modePar1 = 0
        modePar2 = 0
        modePar3 = 0
    elif nInstructionDigits < 4:
        opCode = int(instructionCode[-2:])
        modePar1 = int(instructionCode[0])
        modePar2 = 0
        modePar3 = 0
    elif nInstructionDigits < 5:
        opCode = int(instructionCode[-2:])
        modePar1 = int(instructionCode[1])
        modePar2 = int(instructionCode[0])
        modePar3 = 0
    elif nInstructionDigits < 6:
        opCode = int(instructionCode[-2:])
        modePar1 = int(instructionCode[2])
        modePar2 = int(instructionCode[1])
        modePar3 = int(instructionCode[0])
    
    if opCode != 99:
        if opCode == 1:
            position1 = getParameterPosition(opCodePosition, modePar1, 1, numbers)
            position2 = getParameterPosition(opCodePosition, modePar2, 2, numbers)
            position3 = getParameterPosition(opCodePosition, modePar3, 3, numbers)
            numbers = addition(position1, position2, position3, numbers)
            opCodePosition += 4
        elif opCode == 2:
            position1 = getParameterPosition(opCodePosition, modePar1, 1, numbers)
            position2 = getParameterPosition(opCodePosition, modePar2, 2, numbers)
            position3 = getParameterPosition(opCodePosition, modePar3, 3, numbers)
            numbers = multiplication(position1, position2, position3, numbers)
            opCodePosition += 4
        elif opCode == 3:
            # inputValue = int(input("Please enter the ID for the ship's air conditioner unit: "))
            position = numbers[opCodePosition + 1]
            numbers = setAtPosition(inputValue, position, numbers)
            opCodePosition += 2
        elif opCode == 4:
            position = numbers[opCodePosition + 1]
            output = outputAtPosition(inputValue, position, numbers)
            outputs.append(output)
            opCodePosition += 2
        elif opCode == 5:
            position1 = getParameterPosition(opCodePosition, modePar1, 1, numbers)
            position2 = getParameterPosition(opCodePosition, modePar2, 2, numbers)
            if numbers[position1] > 0:
                opCodePosition = numbers[position2]
            else:
                opCodePosition += 3
        elif opCode == 6:
            position1 = getParameterPosition(opCodePosition, modePar1, 1, numbers)
            position2 = getParameterPosition(opCodePosition, modePar2, 2, numbers)
            if numbers[position1] == 0:
                opCodePosition = numbers[position2]
            else:
                opCodePosition += 3
        elif opCode == 7:
            position1 = getParameterPosition(opCodePosition, modePar1, 1, numbers)
            position2 = getParameterPosition(opCodePosition, modePar2, 2, numbers)
            position3 = getParameterPosition(opCodePosition, modePar3, 3, numbers)
            if numbers[position1] < numbers[position2]:
                numbers[position3] = 1
            else:
                numbers[position3] = 0
            
            opCodePosition += 4
        elif opCode == 8:
            position1 = getParameterPosition(opCodePosition, modePar1, 1, numbers)
            position2 = getParameterPosition(opCodePosition, modePar2, 2, numbers)
            position3 = getParameterPosition(opCodePosition, modePar3, 3, numbers)
            if numbers[position1] == numbers[position2]:
                numbers[position3] = 1
            else:
                numbers[position3] = 0
            
            opCodePosition += 4
        else:
            print('Error - Wrong opCode at position:', opCodePosition, numbers[opCodePosition])
            break

    else:
        print(f'Program halted at position: {opCodePosition}')
        break

print(f'The diagnostic code for system ID {inputValue} is: {outputs[-1]}')

# Advent of Code - Day 6 Part 1 and 2

from collections import defaultdict
    
def splitIntoPair(orbit):
    return orbit.split(')')

orbits = defaultdict(str)
with open('input6.dat', 'r') as orbitsFile:
    for orbit in orbitsFile.read().splitlines():
        orbitPair = splitIntoPair(orbit) 
        orbits[orbitPair[1]] = orbitPair[0]
    orbitsFile.close()

# Part 1
nOrbits = 0
for k, v in orbits.items():
    orbitExists = True
    nOrbits += 1
    orbiter = v
    while orbitExists:
        if orbiter in orbits:
            nOrbits += 1
            orbiter = orbits[orbiter]
        else:
            orbitExists = False

print('Total number of direct and indirect orbits are:', nOrbits)

# Part 2
orbitals = defaultdict(list)
targetOrbiters = ['YOU', 'SAN']
for targetOrbiter in targetOrbiters:
    orbitExists = True
    orbiter = orbits[targetOrbiter]
    while orbitExists:
        if orbiter in orbits:
            orbitals[targetOrbiter].append(orbiter)
            orbiter = orbits[orbiter]
        else:
            orbitExists = False

youToOrigin = set(orbitals[targetOrbiters[0]]).difference(set(orbitals[targetOrbiters[1]]))
sanToOrigin = set(orbitals[targetOrbiters[1]]).difference(set(orbitals[targetOrbiters[0]]))
print('total orbital transfers required for tranfering from YOU to SANTA is', len(youToOrigin) + len(sanToOrigin))