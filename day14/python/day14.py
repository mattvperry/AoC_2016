from hashlib import md5
from re import compile, search
from itertools import count, islice

salt = "yjdafjpo"
trip = compile(r'(.)\1\1')
hashes = {}

def stretchHash(string, stretch):
    for _ in range(stretch + 1):
        string = md5(string.encode('utf-8')).hexdigest()
    return string

def hash(index, stretch):
    if index not in hashes:
        hashes[index] = stretchHash(salt + str(index), stretch)
    return hashes[index]

def triple(string):
    match = trip.search(string)
    return match.group(1) if match else None

def quintuple(string, char):
    quint = r'({})\1\1\1\1'.format(char)
    return search(quint, string)

def day14(stretch):
    triples = ((x, triple(hash(x, stretch))) for x in count())
    triples = ((x, t) for x, t in triples if t)
    return (x for x, t in triples for y in range(x + 1, x + 1000) if quintuple(hash(y, stretch), t))

print(next(islice(day14(0), 63, 64)))
hashes = {}
print(next(islice(day14(2016), 63, 64)))