from re import compile
from itertools import tee, filterfalse, chain

value = compile('value (\d+) goes to (bot \d+)')
botcmp = compile('(bot \d+) gives low to ((?:output|bot) \d+) and high to ((?:output|bot) \d+)')

class Bin:
    def __init__(self, name):
        self.name = name
        self.chips = []
        self.distribute = None

    def give(self, chip):
        self.chips.append(chip)
        if len(self.chips) == 2:
            if 61 in self.chips and 17 in self.chips:
                print(self.name)

            a, b = self.chips
            self.chips = []
            self.distribute(a, b)

def partition(pred, iterable):
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)

def defineBots(cmds, bins):
    for bot, low, high in cmds:
        def dist(a, b, high=high, low=low):
            bins[high].give(max(a, b))
            bins[low].give(min(a, b))
        bins[bot].distribute = dist

def init(values, bins):
    for val, bot in values:
        bins[bot].give(int(val))

def part1(input):
    inputs, cmds = partition(lambda s: s.startswith("bot"), input)
    inputs = [value.match(x).groups() for x in inputs]
    cmds = [botcmp.match(x).groups() for x in cmds]
    bins = {x:Bin(x) for x in chain.from_iterable(cmds)} 
    defineBots(cmds, bins)
    init(inputs, bins)
    return bins['output 0'].chips[0] * bins['output 1'].chips[0] * bins['output 2'].chips[0]

def day10(input):
    return part1(input)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day10(input))