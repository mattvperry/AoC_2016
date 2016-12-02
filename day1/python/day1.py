input = """R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5"""

directions = [
    (0, 1),     # north
    (1, 0),     # east
    (0, -1),    # south
    (-1, 0),    # west
]
turns = {
    'R': lambda dir: (dir + 1) % 4,
    'L': lambda dir: (dir - 1) % 4
}

def distance(loc):
    return sum(map(abs, loc))

def locations():
    currentLoc = (0, 0)
    currentDir = 0
    yield currentLoc
    for move in (x.strip() for x in input.split(",")):
        turn, distance = move[0], int(move[1:])
        currentDir = turns[turn](currentDir)
        for i in range(distance):
            x, y = directions[currentDir]
            currentLoc = (currentLoc[0] + x, currentLoc[1] + y)
            yield currentLoc

visited = list(locations())

# Part 1
print(distance(visited[-1]))

# Part 2
lookup = set()
for visit in visited:
    if visit in lookup:
        print(distance(visit))
        break
    else:
        lookup.add(visit)