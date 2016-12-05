from hashlib import md5
from itertools import count, islice

def indexes(input):
    return (input + str(x) for x in count())

def hashes(inputs):
    return (md5(x.encode('utf-8')).hexdigest() for x in inputs)

def leadingZeroes(hash):
    return hash.startswith("00000")

def validRange(hash):
    return hash[5].isdigit() and 0 <= int(hash[5]) <= 7

def part1(input):
    return "".join(islice((x[5] for x in hashes(indexes(input)) if leadingZeroes(x)), 0, 8)) 

def part2(input):
    ans = [' '] * 8
    validHashes = (x for x in hashes(indexes(input)) if leadingZeroes(x) and validRange(x))
    while ' ' in ans:
        hash = next(validHashes)
        if ans[int(hash[5])] != ' ':
            continue
        ans[int(hash[5])] = hash[6]
    return ans

def day5(input):
    return part2(input)

print(day5("ugkcyxxp"))