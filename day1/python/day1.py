from collections import defaultdict

input = """R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5"""

north = (1, 0)
south = (-1, 0)
east = (0, 1)
west = (0, -1)

visited = defaultdict(int)
visited[(0, 0)] += 1

def day1(inputs):
    direction = north
    curr = (0, 0)
    for dir, num in inputs:
        if direction == north and dir == 'R':
            direction = east
        elif direction == north and dir == 'L':
            direction = west
        elif direction == south and dir == 'R':
            direction = west
        elif direction == south and dir == 'L':
            direction = east
        elif direction == east and dir == 'L':
            direction = north
        elif direction == east and dir == 'R':
            direction = south
        elif direction == west and dir == 'R':
            direction = north
        elif direction == west and dir == 'L':
            direction = south
        for i in range(num):
            curr = (curr[0] + direction[0], curr[1] + direction[1])
            visited[curr] += 1
            if visited[curr] == 2:
                return abs(curr[0]) + abs(curr[1])

print(day1([(x.strip()[0], int(x.strip()[1:])) for x in input.split(",")]))
