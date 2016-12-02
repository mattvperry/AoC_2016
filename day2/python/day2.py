input = """
DDDURLURURUDLDURRURULLRRDULRRLRLRURDLRRDUDRUDLRDUUDRRUDLLLURLUURLRURURLRLUDDURUULDURDRUUDLLDDDRLDUULLUDURRLUULUULDLDDULRLDLURURUULRURDULLLURLDRDULLULRRRLRLRULLULRULUUULRLLURURDLLRURRUUUDURRDLURUURDDLRRLUURLRRULURRDDRDULLLDRDDDDURURLLULDDULLRLDRLRRDLLURLRRUDDDRDLLRUDLLLLRLLRUDDLUUDRLRRRDRLRDLRRULRUUDUUDULLRLUDLLDDLLDLUDRURLULDLRDDLDRUDLDDLDDDRLLDUURRUUDLLULLRLDLUURRLLDRDLRRRRUUUURLUUUULRRUDDUDDRLDDURLRLRLLRRUDRDLRLDRRRRRRUDDURUUUUDDUDUDU
RLULUULRDDRLULRDDLRDUURLRUDDDUULUUUDDRDRRRLDUURDURDRLLLRDDRLURLDRRDLRLUURULUURDRRULRULDULDLRRDDRLDRUDUDDUDDRULURLULUDRDUDDDULRRRURLRRDLRDLDLLRLUULURLDRURRRLLURRRRRLLULRRRDDLRLDDUULDLLRDDRLLUUDRURLRULULRLRUULUUUUUDRURLURLDDUDDLRDDLDRRLDLURULUUDRDLULLURDLLLRRDRURUDDURRLURRDURURDLRUDRULUULLDRLRRDRLDDUDRDLLRURURLUDUURUULDURUDULRLRDLDURRLLDRDUDRUDDRLRURUDDLRRDLLLDULRRDRDRRRLURLDLURRDULDURUUUDURLDLRURRDRULLDDLLLRUULLLLURRRLLLDRRUDDDLURLRRRDRLRDLUUUDDRULLUULDURLDUUURUDRURUDRDLRRLDRURRLRDDLLLULUDDUULDURLRUDRDDD
RDDRUDLRLDDDRLRRLRRLUULDRLRUUURULRRLUURLLLRLULDDLDLRLULULUUDDDRLLLUDLLRUDURUDDLLDUDLURRULLRDLDURULRLDRLDLDRDDRUDRUULLLLRULULLLDDDULUUDUUDDLDRLRRDLRLURRLLDRLDLDLULRLRDLDLRLUULLDLULRRRDDRUULDUDLUUUUDUDRLUURDURRULLDRURUDURDUULRRULUULULRLDRLRLLRRRLULURLUDULLDRLDRDRULLUUUDLDUUUDLRDULRDDDDDDDDLLRDULLUDRDDRURUDDLURRUULUURURDUDLLRRRRDUDLURLLURURLRDLDUUDRURULRDURDLDRUDLRRLDLDULRRUDRDUUDRLURUURLDLUDLLRDDRDU
LLDDDDLUDLLDUDURRURLLLLRLRRLDULLURULDULDLDLLDRRDLUDRULLRUUURDRLLURDDLLUDDLRLLRDDLULRLDDRURLUDRDULLRUDDLUURULUUURURLRULRLDLDDLRDLDLLRUURDLUDRRRDDRDRLLUDDRLDRLLLRULRDLLRLRRDDLDRDDDUDUDLUULDLDUDDLRLDUULRULDLDULDDRRLUUURUUUDLRDRULDRRLLURRRDUDULDUDUDULLULLULULURLLRRLDULDULDLRDDRRLRDRLDRLUDLLLUULLRLLRLDRDDRUDDRLLDDLRULLLULRDDDLLLDRDLRULDDDLULURDULRLDRLULDDLRUDDUDLDDDUDRDRULULDDLDLRRDURLLRLLDDURRLRRULLURLRUDDLUURULULURLRUDLLLUDDURRLURLLRLLRRLDULRRUDURLLDDRLDLRRLULUULRRUURRRDULRLRLRDDRDULULUUDULLLLURULURRUDRLL
UULLULRUULUUUUDDRULLRLDDLRLDDLULURDDLULURDRULUURDLLUDDLDRLUDLLRUURRUDRLDRDDRRLLRULDLLRUUULLLDLDDULDRLRURLDRDUURLURDRUURUULURLRLRRURLDDDLLDDLDDDULRUDLURULLDDRLDLUDURLLLLLRULRRLLUDRUURLLURRLLRDRLLLRRDDDRRRDLRDRDUDDRLLRRDRLRLDDDLURUUUUULDULDRRRRLUDRLRDRUDUDDRULDULULDRUUDUULLUDULRLRRURDLDDUDDRDULLUURLDRDLDDUURULRDLUDDLDURUDRRRDUDRRDRLRLULDRDRLRLRRUDLLLDDDRURDRLRUDRRDDLDRRLRRDLUURLRDRRUDRRDLDDDLRDDLRDUUURRRUULLDDDLLRLDRRLLDDRLRRRLUDLRURULLDULLLUDLDLRLLDDRDRUDLRRDDLUU
"""

_, A, B, C, D = 0, 'A', 'B', 'C', 'D'

keypad1 = [
    [_, _, _, _, _],
    [_, 1, 2, 3, _],
    [_, 4, 5, 6, _],
    [_, 7, 8, 9, _],
    [_, _, _, _, _]
]

keypad2 = [
    [_, _, _, _, _, _, _],
    [_, _, _, 1, _, _, _],
    [_, _, 2, 3, 4, _, _],
    [_, 5, 6, 7, 8, 9, _],
    [_, _, A, B, C, _, _],
    [_, _, _, D, _, _, _],
    [_, _, _, _, _, _, _]
]

def makeMoves(keypad):
    return {
        'U': lambda loc: (loc[0], loc[1] - 1),
        'D': lambda loc: (loc[0], loc[1] + 1),
        'L': lambda loc: (loc[0] - 1, loc[1]),
        'R': lambda loc: (loc[0] + 1, loc[1])
    }

def keys(input, keypad, currentLoc):
    moves = makeMoves(keypad)
    for num in (x for x in input.strip().split("\n")):
        for move in num:
            newX, newY = moves[move](currentLoc)
            currentLoc = (newX, newY) if keypad[newX][newY] != _ else currentLoc
        yield currentLoc

print("".join([str(keypad1[y][x]) for x, y in keys(input, keypad1, (2, 2))]))
print("".join([str(keypad2[y][x]) for x, y in keys(input, keypad2, (1, 3))]))