from collections import Counter

def frequencies(words):
    return (Counter(x).most_common() for x in zip(*words))

def frequent(input, index):
    return "".join(x[index][0] for x in frequencies(input))

def day6(input):
    return frequent(input, 0), frequent(input, -1)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day6(input))