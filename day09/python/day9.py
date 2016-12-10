from re import compile

marker = compile(r'^\((\d+)x(\d+)\)')

def decompress(line, rec=False):
    if line == "":
        return 0

    match = marker.match(line)
    if match:
        length, times = map(int, match.groups())
        remainder = line[len(match.group(0)):]
        x = decompress(remainder[:length], rec) if rec else length
        return x * times + decompress(remainder[length:], rec)
    else:
        return 1 + decompress(line[1:])

def day9(input):
    return decompress(input), decompress(input, True)

input = open("../input.txt").read()
print(day9(input))