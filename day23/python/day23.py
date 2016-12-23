from re import compile

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

def toggle(val, state):
    pc, regs, code = state
    val = lookup(val, state)
    if not 0 <= pc + val < len(code):
        return state

    ins, *args = code[pc + val]
    new = {
        'inc': 'dec',
        'dec': 'inc',
        'tgl': 'inc',
        'jnz': 'cpy',
        'cpy': 'jnz',
        'mul': 'jnz'
    }[ins]
    code[pc + val] = (new, *args)
    return (pc, regs, code)

def halted(state):
    pc, _, code = state
    return pc >= len(code)

def execute(input, a):
    c = [instr.match(x).groups() for x in input]
    state = (0, { 'a': a, 'b': 0, 'c': 0, 'd': 0 }, c)
    proc = {
        'cpy': lambda x, y, z: setReg(y, lookup(x, state), state),
        'inc': lambda x, y, z: setReg(x, lookup(x, state) + 1, state),
        'dec': lambda x, y, z: setReg(x, lookup(x, state) - 1, state),
        'jnz': lambda x, y, z: setPc(lookup(y, state) - 1, state) if lookup(x, state) != 0 else state,
        'tgl': lambda x, y, z: toggle(x, state),
        'mul': lambda x, y, z: setReg(z, lookup(z, state) + lookup(x, state) * lookup(y, state), state)
    }

    while not halted(state):
        pc, regs, code = state
        ins, *args = code[pc]
        pc, regs, code = proc[ins](*args)
        state = (pc + 1, regs, code)

    return state

def day23(input, a):
    pc, regs, code = execute(input, a)
    return regs['a']

input1 = open("../input.txt").read()
input1 = [x.strip() for x in input1.split("\n")]
print(day23(input1, 7))

input2 = open("../input.2.txt").read()
input2 = [x.strip() for x in input2.split("\n")]
print(day23(input2, 12))