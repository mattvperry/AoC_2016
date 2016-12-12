from operator import itemgetter
from itertools import combinations, chain, product, groupby
from random import choice

import pprint
pp = pprint.PrettyPrinter(indent = 2)

def validCombo(items):
    elems = {k:list(map(itemgetter(1), v)) for k, v in groupby(items, itemgetter(0))}
    # Has a generator
    hasGen = 'G' in map(itemgetter(1), items)
    # Has an unprotected microchip
    loneM = any(k for k, v in elems.items() if not 'G' in v and 'M' in v)
    return not (hasGen and loneM)

def validMoves(state):
    elevator, floors = state
    floor = floors[elevator]
    # Valid sets of items to take on elevator
    combos = chain(map(lambda x: [x], floor), filter(validCombo, combinations(floor, 2)))
    # Valid directions to move elevator
    dirs = filter(lambda  d: elevator + d in range(4), (1, -1))
    # Cartesian product of directions to move elevator and sets of items to take
    return product(dirs, combos)

def validFloors(floors):
    return all(map(validCombo, floors))

def makeMove(state, move):
    elevator, floors = state
    newFloors = floors[:]
    direction, itemSet = move
    newFloors[elevator] = [x for x in newFloors[elevator] if x not in itemSet]
    newFloors[elevator + direction] = newFloors[elevator + direction] + list(itemSet)    
    return elevator + direction, newFloors

def stateEq(state1, state2):
    (e1, f1), (e2, f2) = state1, state2
    return e1 == e2 and all(set(x) == set(y) for x, y in zip(f1, f2))

def makeAllMoves(state, prevStates):
    states = (makeMove(state, move) for move in validMoves(state))
    states = ((e, f) for e, f in states if validFloors(f))
    return (s for s in states if not any(stateEq(s, p) for p in prevStates))

def finished(state):
    _, floors = state
    sizes = list(map(len, floors))
    return all(x == 0 for x in sizes[1:])

"""
def bfs(state):
    queue = [(state, [state])]
    while queue:
        (s, path) = queue.pop(0)
        for next in makeAllMoves(s, path):
            if finished(next):
                yield path + [next]
            else:
                queue.append((next, path + [next]))

"""
def bfs(state):
    steps = 0
    visited, queue = [], [state]
    while not any(1 for s in queue if finished(s)):
        print(steps, len(queue))
        visited = visited + queue
        queue = [n for s in queue for n in makeAllMoves(s, visited)]
        steps += 1
    return steps

def day11(elevator, floors):
    """
    final = next(bfs((elevator, floors)))
    pp.pprint(final)
    return len(final) - 1
    """
    return bfs((elevator, floors))

# Initial State
elevator = 3
"""
floors = [
    [],
    [('Co', 'M'), ('Cu', 'M'), ('Ru', 'M'), ('Pl', 'M')],
    [('Co', 'G'), ('Cu', 'G'), ('Ru', 'G'), ('Pl', 'G')],
    [('Pr', 'G'), ('Pr', 'M')]
]

"""
floors = [
    [],
    [('L', 'G')],
    [('H', 'G')],
    [('H', 'M'), ('L', 'M')]
]

print(day11(elevator, floors))