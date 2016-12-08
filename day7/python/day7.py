from re import split, search, finditer
from itertools import zip_longest, chain, product

def splitIp(ip):
    separated = split(r'(?:\[|\])', ip)
    return zip(*zip_longest(*[iter(separated)] * 2, fillvalue='')) 

def hasAbba(text):
    return search(r'(.)(?!\1)(.)\2\1', text)

def findBabs(text):
    matches = (m.groups() for m in finditer(r'(?=((.)(?!\2)(.)\2))', text))
    return (z + y + z for x, y, z in matches)

def supportsTls(ip):
    supernet, hypernet = splitIp(ip)
    return any(hasAbba(x) for x in supernet) and not any(hasAbba(x) for x in hypernet)

def toBab(aba):
    return "".join([aba[1], aba[0], aba[1]])

def supportsSsl(ip):
    supernet, hypernet = splitIp(ip)
    babs = chain(*(findBabs(x) for x in supernet)) 
    return any((x in y) for x, y in product(babs, hypernet))

def part1(input):
    return sum(map(supportsTls, input))

def part2(input):
    return sum(map(supportsSsl, input))

def day7(input):
    return part1(input), part2(input)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day7(input))