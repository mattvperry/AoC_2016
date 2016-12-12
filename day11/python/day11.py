from operator import itemgetter
from itertools import combinations, chain, product, groupby
from heapq import heappush, heappop

def validFloor(floor):
    if not floor or floor[-1] < 0:
        return True
    return all(-chip in floor for chip in floor if chip < 0)

def moves(state):
    elevator, floors = state
    floor = floors[elevator]
    # Sets of items to take on elevator
    combos = chain(map(lambda x: (x,), floor), combinations(floor, 2))
    # Valid directions to move elevator
    dirs = filter(lambda  d: 0 <= elevator + d < 4, (1, -1))
    # Cartesian product of directions to move elevator and sets of items to take
    return product(dirs, combos)

def makeValidMove(state, move):
    elevator, floors = state
    direction, itemSet = move

    newFloors = list(floors)
    newFloors[elevator] = tuple(x for x in floors[elevator] if x not in itemSet)
    newFloors[elevator + direction] = tuple(sorted(floors[elevator + direction] + itemSet))

    if validFloor(newFloors[elevator]) and validFloor(newFloors[elevator + direction]):
        return elevator + direction, tuple(newFloors)

def makeAllMoves(state):
    states = (makeValidMove(state, move) for move in moves(state))
    return (s for s in states if s)

def aStar(initial):
    queue = []
    heappush(queue, (0, initial))
    cost = { initial: 0 }

    while queue:
        _, state = heappop(queue)
        e, f = state
        if all(x == () for x in f[1:]):
            return cost[state]
        
        for next in makeAllMoves(state):
            newCost = cost[state] + 1
            if next not in cost or newCost < cost[next]:
                cost[next] = newCost
                prio = newCost - len(next[1][0]) * 10
                heappush(queue, (prio, next))

def day11(elevator, floors):
    return aStar((elevator, floors))

pr, co, cu, ru, pl, el, di = 1, 2, 3, 4, 5, 6, 7
elevator = 3
floors1 = (
    (),
    tuple(sorted((-co, -cu, -ru, -pl))),
    tuple(sorted(( co,  cu,  ru,  pl))),
    tuple(sorted(( pr, -pr)))
)
floors2 = (
    (),
    tuple(sorted((-co, -cu, -ru, -pl))),
    tuple(sorted(( co,  cu,  ru,  pl))),
    tuple(sorted(( pr, -pr,  el, -el,  di, -di)))
)

print(day11(elevator, floors1))