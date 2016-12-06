from collections import Counter

def frequencies(words):
    return (Counter(x).most_common() for x in zip(*words))

def part1(input):
    return "".join(x[0][0] for x in frequencies(input))

def part2(input):
    return "".join(x[-1][0] for x in frequencies(input))

def day6(input):
    return part1(input), part2(input)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day6(input))