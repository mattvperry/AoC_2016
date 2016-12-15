from itertools import islice, count

discs = [
    (0, 7),
    (0, 13),
    (2, 3),
    (2, 5),
    (0, 17),
    (7, 19)
]

def isSlot(disc, time):
    offset, pos = disc
    return (offset + time) % pos == 0

def day15(discs):
    for x in count():
        run = range(x + 1, x + 1 + len(discs))
        if all(isSlot(d, t) for d, t in zip(discs, run)):
            yield x

print(next(day15(discs)))
print(next(day15(discs + [(0, 11)])))