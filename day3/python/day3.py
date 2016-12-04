def chunk(list, size):
    n = max(1, size)
    return (list[i:i + n] for i in range(0, len(list), n))

def valids(sides):
    return sum((1 for x, y, z in sides if x + y > z and y + z > x and x + z > y))

def triangles(input):
    return (map(int, t.split()) for t in input)

def day3(input):
    transposed = (chunk(x, 3) for x in map(list, zip(*triangles(input))))
    return valids(triangles(input)), sum(map(valids, transposed))

input = open("../input.txt").read()
print(day3([x.strip() for x in input.strip().split("\n")]))