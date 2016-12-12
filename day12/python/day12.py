from re import compile

instr = compile(r'(\w\w\w) ([^\s]*)(?: ([^\s]*))?')

def makeProcessor(state):
    regOrInt = lambda x: int(state['regs'][x]) if x in state['regs'] else int(x)
    def setReg(name, val):
        state['regs'][name] = val
    
    def setPc(val):
        state['pc'] = val

    return {
        'cpy': lambda x, y: setReg(y, regOrInt(x)),
        'inc': lambda x, _: setReg(x, state['regs'][x] + 1),
        'dec': lambda x, _: setReg(x, state['regs'][x] - 1),
        'jnz': lambda x, y: setPc(state['pc'] + regOrInt(y) - 1 if regOrInt(x) != 0 else state['pc'])
    }

def execute(input):
    state = {
        'pc': 0,
        'regs': { 'a': 0, 'b': 0, 'c': 1, 'd': 0 }
    }

    proc = makeProcessor(state)
    code = [instr.match(x).groups() for x in input]
    while state['pc'] < len(code):
        ins, *args = code[state['pc']]
        proc[ins](*args)
        state['pc'] += 1
    return state['regs']

def day12(input):
    return execute(input)

input = open("../input.txt").read()
input = [x.strip() for x in input.split("\n")]
print(day12(input))