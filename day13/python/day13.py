from itertools import chain

input = 1352

def open(x, y):
    num = (x * x + 3 * x + 2 * x * y + y + y * y) + input
    num = num - ((num >> 1) & 0x55555555)
    num = (num & 0x33333333) + ((num >> 2) & 0x33333333)
    num = (((num + (num >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24
    return num % 2 == 0

def neighbors(point):
    x, y = point
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = ((x + a, y + b) for a, b in dirs if x + a >= 0 and y + b >= 0)
    return {(a, b) for a, b in neighbors if open(a, b)}

def bfs_paths(start, end):
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)
        for next in neighbors(vertex) - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def bfs(start):
    visited = set([start])
    for _ in range(50):
        allNeighbors = chain.from_iterable(neighbors(v) for v in visited)
        visited |= set(allNeighbors)
    return visited

def part1():
    return len(next(bfs_paths((1, 1), (31, 39)))) - 1

def part2():
    return len(bfs((1, 1)))

def day12():
    return part1(), part2()

print(day12())