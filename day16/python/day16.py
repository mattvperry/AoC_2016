from itertools import chain

def invert(bit):
    return "1" if bit == "0" else "0"

def process(data):
    inverted = (invert(x) for x in reversed(data))
    return ''.join(chain(data, "0", inverted))

def checkbits(bits):
    a, b = bits
    return "1" if a == b else "0"

def checksum(data):
    return [checkbits(b) for b in zip(data[0::2], data[1::2])]

def day16(data, length):
    while len(data) < length:
        data = process(data)
    
    data = checksum(data[:length])
    while len(data) % 2 == 0:
        data = checksum(data)

    return ''.join(data)

print(day16("00101000101111010", 272))
print(day16("00101000101111010", 35651584))