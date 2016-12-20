def merge(ints):
    ints.sort()
    stack = [ints[0]]
    for start, end in ints[1:]:
        ts, te = stack[-1]
        if te <= start:
            stack.append((start, end))
        elif te < end:
            stack.pop()
            stack.append((ts, end))
    return stack

def day20(input):
    intervals = merge([tuple(map(int, l.split("-"))) for l in input])
    part1 = intervals[0][1] + 1
    part2 = sum(c - b - 1 for (a, b), (c, d) in zip(intervals, intervals[1:]))
    return part1, part2

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day20(input))