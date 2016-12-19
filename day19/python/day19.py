from itertools import cycle
from collections import defaultdict

elves = 3014603

def part1():
    curr = 0
    presents = set(range(elves))
    while len(presents) > 1:
        print(len(presents))
        while not curr in presents:
            curr = (curr + 1) % elves
        neigh = (curr + 1) % elves
        while not neigh in presents:
            neigh = (neigh + 1) % elves
        presents.remove(neigh)
        curr = (neigh + 1) % elves
    return next(p + 1 for p in presents)

print(part1())