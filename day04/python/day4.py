from re import match
from collections import Counter
from string import ascii_lowercase

def parseRoom(line):
    line = line.split('-')
    id, checksum = match(r'(\d+)\[([a-z]+)\]', line[-1]).groups()
    return "-".join(line[:-1]), int(id), checksum

def validRoom(name, checksum):
    count = Counter(name.replace('-', '')).items()
    count = sorted((v * -1, k) for k, v in count)
    return "".join(c for _, c in count[:5]) == (checksum)

def decryptChar(char, inc):
    if char == '-':
        return ' '
    return ascii_lowercase[(ascii_lowercase.index(char) + inc) % len(ascii_lowercase)]

def decryptName(name, id):
    return "".join(decryptChar(char, id) for char in name)

def part1(rooms):
    return sum(id for name, id in rooms)

def part2(rooms):
    for name, id in rooms:
        if 'northpole' in decryptName(name, id):
            return id

def day4(input):
    validRooms = [(name, id) for name, id, csc in map(parseRoom, input) if validRoom(name, csc)]
    return part1(validRooms), part2(validRooms)

input = open("../input.txt").read()
print(day4([x.strip() for x in input.strip().split("\n")]))