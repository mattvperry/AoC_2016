from itertools import islice, chain

input = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."

def nextRow(prev):
    prev = [True] + prev + [True]
    for l, c, r in zip(prev, prev[1:], prev[2:]):
        yield l == r

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