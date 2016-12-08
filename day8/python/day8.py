from re import compile
from functools import reduce

rectRe = compile(r'(rect) (\d+)x(\d+)')
rotaRe = compile(r'(rotate [rc])\w* \w=(\d+) by (\d+)')

def makeScreen(x, y):
    return [[' '] * x for _ in range(y)]

def transpose(l):
    return list(map(list, zip(*l)))

def parseInstruction(inst):
    rect = rectRe.search(inst)
    rota = rotaRe.search(inst)
    a, b, c = rect.groups() if rect else rota.groups()
    return a, int(b), int(c)

def fill(x, y, screen):
    return [['#'] * x + r[x:] for r in screen[:y]] + screen[y:]

def rotate(a, b, screen):
    newRow = screen[a][-b:] + screen[a][:-b]
    return screen[:a] + [newRow] + screen[a + 1:]

def light(input):
    instMap = {
        'rect':     fill,
        'rotate r': rotate,
        'rotate c': lambda a, b, s: transpose(rotate(a, b, transpose(s))) 
    }
    screen = makeScreen(50, 6)
    for cmd, a, b in map(parseInstruction, input):
        screen = instMap[cmd](a, b, screen)
    return screen

def day8(input):
    screen = light(input)
    print(sum(r.count('#') for r in screen))
    return "\n".join("".join(x) for x in screen)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day8(input))