from re import compile

rectRe = compile(r'(rect)( )(\d+)x(\d+)')
rotaRe = compile(r'(rotate) (row|column) \w=(\d+) by (\d+)')

def makeScreen(x, y):
    return [[' '] * x for _ in range(y)]

def transpose(l):
    return list(map(list, zip(*l)))

def parseInstruction(inst):
    rect = rectRe.search(inst)
    rota = rotaRe.search(inst)
    return rect.groups() if rect else rota.groups()

def fillRect(x, y, screen):
    return [['#'] * x + r[x:] for r in screen[:y]] + screen[y:]

def rotateRow(a, b, screen):
    newRow = screen[a][-b:] + screen[a][:-b]
    return screen[:a] + [newRow] + screen[a + 1:]

def rotateCol(a, b, screen):
    screen = transpose(screen)
    screen = rotateRow(a, b, screen)
    return transpose(screen)

def countLit(screen):
    return sum(map(lambda x: x.count('#'), screen))

def lightScreen(input):
    screen = makeScreen(50, 6)
    for cmd, place, dim1, dim2 in map(parseInstruction, input):
        if cmd == 'rect':
            screen = fillRect(int(dim1), int(dim2), screen)
        if cmd == 'rotate' and place == 'row':
            screen = rotateRow(int(dim1), int(dim2), screen)
        if cmd == 'rotate' and place == 'column':
            screen = rotateCol(int(dim1), int(dim2), screen)
    return screen

def day8(input):
    screen = lightScreen(input)
    print(countLit(screen))
    return "\n".join("".join(x) for x in screen)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day8(input))