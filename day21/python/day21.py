from re import compile
from itertools import chain

swapPosRegex = compile(r'swap position (\d) with position (\d)')
swapLetterRegex = compile(r'swap letter (\w) with letter (\w)')
rotateRegex = compile(r'rotate (left|right) (\d) steps?')
rotatePosRegex = compile(r'rotate based on position of letter (\w)')
reverseRegex = compile(r'reverse positions (\d) through (\d)')
moveRegex = compile(r'move position (\d) to position (\d)')

def swapPos(pword, x, y):
    pword[x], pword[y] = pword[y], pword[x]
    return pword

def swapLetter(pword, x, y):
    return swapPos(pword, pword.index(x), pword.index(y))

def rotate(pword, dir, x):
    l = len(pword)
    return pword[(dir * x) % l:] + pword[:(dir * x) % l]

def rotatePos(pword, x):
    n = pword.index(x)
    return rotate(pword, -1, 1 + n + (0 if n < 4 else 1))

def reverse(pword, x, y):
    return list(chain(pword[:x], reversed(pword[x:y + 1]), pword[y + 1:]))

def move(pword, x, y):
    z = pword.pop(x)
    pword.insert(y, z)
    return pword

def revRotatePos(pword, x):
    pw = pword[::]
    while rotatePos(pw, x) != pword:
        pw = rotate(pw, 1, 1)
    return pw

def part1(password, input):
    password = list(password)
    for ins in input:
        if ins.startswith("swap position"):
            match = swapPosRegex.match(ins)
            password = swapPos(password, *map(int, match.groups()))
        elif ins.startswith("swap letter"):
            match = swapLetterRegex.match(ins)
            password = swapLetter(password, *match.groups())
        elif ins.startswith("rotate based"):
            match = rotatePosRegex.match(ins)
            password = rotatePos(password, *match.groups())
        elif ins.startswith("rotate"):
            d, s = rotateRegex.match(ins).groups()
            password = rotate(password, (1 if d == 'left' else -1), int(s))
        elif ins.startswith("reverse"):
            match = reverseRegex.match(ins)
            password = reverse(password, *map(int, match.groups()))
        elif ins.startswith("move"):
            match = moveRegex.match(ins)
            password = move(password, *map(int, match.groups()))
    return ''.join(password)

def part2(password, input):
    password = list(password)
    for ins in reversed(input):
        if ins.startswith("swap position"):
            match = swapPosRegex.match(ins)
            password = swapPos(password, *map(int, match.groups()))
        elif ins.startswith("swap letter"):
            match = swapLetterRegex.match(ins)
            password = swapLetter(password, *match.groups())
        elif ins.startswith("rotate based"):
            match = rotatePosRegex.match(ins)
            password = revRotatePos(password, *match.groups())
        elif ins.startswith("rotate"):
            d, s = rotateRegex.match(ins).groups()
            password = rotate(password, (-1 if d == 'left' else 1), int(s))
        elif ins.startswith("reverse"):
            match = reverseRegex.match(ins)
            password = reverse(password, *map(int, match.groups()))
        elif ins.startswith("move"):
            match = moveRegex.match(ins)
            password = move(password, *reversed(list(map(int, match.groups()))))
    return ''.join(password)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(part1("abcdefgh", input))
print(part2("fbgdceah", input))