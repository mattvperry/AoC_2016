from re import compile

instr = compile(r'(\w\w\w) ([^\s]*)(?: ([^\s]*))?')

def lookup(param, state):
    _, regs = state
    return int(regs[param]) if param in regs else int(param)

def setReg(to, val, state):
    pc, regs = state
    regs[to] = val
    return (pc, regs)

def setPc(val, state):
    pc, regs = state
    return (pc + val, regs)

def halted(state, code):
    pc, _ = state
    return pc >= len(code)

def execute(input):
    code = [instr.match(x).groups() for x in input]
    state = (0, { 'a': 0, 'b': 0, 'c': 1, 'd': 0 })
    proc = {
        'cpy': lambda x, y: setReg(y, lookup(x, state), state),
        'inc': lambda x, _: setReg(x, lookup(x, state) + 1, state),
        'dec': lambda x, _: setReg(x, lookup(x, state) - 1, state),
        'jnz': lambda x, y: setPc(lookup(y, state) - 1, state) if lookup(x, state) != 0 else state
    }

    while not halted(state, code):
        pc, regs = state
        ins, *args = code[pc]
        pc, regs = proc[ins](*args)
        state = (pc + 1, regs)

    return state

def day12(input):
    return execute(input)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day12(input))