def part1(input):
    return input

def part2(input):
    pass

def day10(input):
    return part1(input), part2(input)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day10(input))