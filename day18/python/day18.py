from itertools import islice, chain

input = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."

def nextRow(prev):
    prev = [True] + prev + [True]
    for p in zip(prev, prev[1:], prev[2:]):
        if p in [(False, False, True), (True, False, False), (False, True, True), (True, True, False)]:
            yield False
        else:
            yield True

def makeRows(row):
    yield row
    while True:
        row = list(nextRow(row))
        yield row

def day18():
    convert = lambda x: True if x == '.' else False
    rows = makeRows([convert(x) for x in input])
    part1 = list(chain(*islice(rows, 40))).count(True)
    part2 = list(chain(*islice(rows, 399960))).count(True)
    return part1, part1 + part2

print(day18())