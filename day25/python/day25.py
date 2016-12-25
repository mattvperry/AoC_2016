from re import compile
from itertools import count

instr = compile(r'(\w\w\w) ([^\s]*)(?: ([^\s]*))?(?: ([^\s]*))?')

def lookup(param, state):
    _, regs, _ = state
    return int(regs[param]) if param in regs else int(param)

def setReg(to, val, state):
    pc, regs, _ = state
    regs[to] = val
    return (pc, regs, _)

def setPc(val, state):
    pc, regs, _ = state
    return (pc + val, regs, _)

def output(val, state):
    pc, regs, out = state
    return (pc, regs, out + [lookup(val, state)])

def halted(state):
    pc, _, out = state
    return len(out) >= 8

def execute(input, a):
    code = [instr.match(x).groups() for x in input]
    state = (0, { 'a': a, 'b': 0, 'c': 0, 'd': 0 }, [])
    proc = {
        'cpy': lambda x, y, z: setReg(y, lookup(x, state), state),
        'inc': lambda x, y, z: setReg(x, lookup(x, state) + 1, state),
        'dec': lambda x, y, z: setReg(x, lookup(x, state) - 1, state),
        'jnz': lambda x, y, z: setPc(lookup(y, state) - 1, state) if lookup(x, state) != 0 else state,
        'mul': lambda x, y, z: setReg(z, lookup(z, state) + lookup(x, state) * lookup(y, state), state),
        'out': lambda x, y, z: output(x, state)
    }

    while not halted(state):
        pc, regs, out = state
        ins, *args = code[pc]
        pc, regs, out = proc[ins](*args)
        state = (pc + 1, regs, out)

    return state

def day25(input):
    for i in count():
        pc, regs, out = execute(input, i)
        if out == [0, 1, 0, 1, 0, 1, 0, 1]:
            return i

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day25(input))