from itertools import combinations, permutations
from heapq import heappush, heappop

def inside(x, y, input):
    return 0 <= x <= len(input[0]) and 0 <= y <= len(input)

def neighbors(point, input):
    x, y = point
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = ((x + a, y + b) for a, b in dirs if inside(x + a, y + b, input))
    return {(a, b) for a, b in neighbors if input[b][a] != '#'}

def goals(input):
    for y in range(len(input)):
        row = input[y]
        for x in range(len(row)):
            if row[x].isdigit():
                yield int(row[x]), (x, y)

def dist(start, end):
    (x1, y1), (x2, y2) = start, end
    return abs(x1 - x2) + abs(y1 - y2)

def aStar(start, goal, input):
    queue = []
    heappush(queue, (0, start))
    cost = { start: 0 }

    while queue:
        _, current = heappop(queue)
        if current == goal:
            return cost[current]

        for next in neighbors(current, input):
            newCost = cost[current] + 1
            if next not in cost or newCost < cost[next]:
                cost[next] = newCost
                prio = newCost + dist(next, goal)
                heappush(queue, (prio, next))

def minLen(perms, dists):
    permPairs = (zip(perm, perm[1:]) for perm in perms)
    return min(sum(dists[tuple(sorted(p))] for p in ps) for ps in permPairs)

def day24(input):
    gs = {k:v for k, v in goals(input)}
    pairs = (tuple(sorted(c)) for c in combinations(gs.keys(), 2))
    dists = {(s, e):aStar(gs[s], gs[e], input) for s, e in pairs}

    igs = list(range(1, len(gs.keys())))
    perms1 = ([0] + list(p) for p in permutations(igs))
    perms2 = ([0] + list(p) + [0] for p in permutations(igs))
    return minLen(perms1, dists), minLen(perms2, dists)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day24(input))