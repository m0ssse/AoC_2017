def part1(program):
    registers = {}
    i = 0
    freq = 0
    while i<len(program):
        command = program[i]
        i+=1
        parts = command.split()
        if parts[0]=="snd":
            freq = get_value(parts[1], registers)
        elif parts[0]=="set":
            x, y = parts[1:]
            if x not in registers:
                registers[x] = 0
            registers[x] = get_value(y, registers)

        elif parts[0]=="add":
            x, y = parts[1:]
            if x not in registers:
                registers[x] = 0
            registers[x]+=get_value(y, registers)

        elif parts[0]=="mul":
            x, y = parts[1:]
            if x not in registers:
                registers[x] = 0
            registers[x]*=get_value(y, registers)
       
        elif parts[0]=="mod":
            x, y = parts[1:]
            if x not in registers:
                registers[x] = 0
            registers[x]%=get_value(y, registers)

        elif parts[0]=="rcv":
            x = get_value(parts[1], registers)
            if x:
                break

        elif parts[0]=="jgz":
            x, y = [get_value(z, registers) for z in parts[1:]]
            if x>0:
                i+=y-1
    print(freq)

def get_value(x, registers):
    try:
        x = int(x)
    except ValueError:
        if x not in registers:
            registers[x] = 0
        x = registers[x]
    return x

def execute(i, registers, program, freq):
    command = program[i]
    i+=1
    parts = command.split()

    if parts[0]=="set":
        x, y = parts[1:]
        if x not in registers:
            registers[x] = 0
        registers[x] = get_value(y, registers)

    elif parts[0]=="add":
        x, y = parts[1:]
        if x not in registers:
            registers[x] = 0
        registers[x]+=get_value(y, registers)

    elif parts[0]=="mul":
        x, y = parts[1:]
        if x not in registers:
            registers[x] = 0
        registers[x]*=get_value(y, registers)
    
    elif parts[0]=="mod":
        x, y = parts[1:]
        if x not in registers:
            registers[x] = 0
        registers[x]%=get_value(y, registers)

    elif parts[0]=="jgz":
        x, y = [get_value(z, registers) for z in parts[1:]]
        if x>0:
            i+=y-1
    
    elif parts[0]=="snd":
        freq = get_value(parts[1], registers)

    return i, freq

def part2(program):
    registers0 = {"p": 0}
    registers1 = {"p": 1}
    program0_done = False
    program1_done = False
    program0_halted = False
    program1_halted = False
    queue0 = []
    res = 0
    queue0, queue1 = [], []
    i0, i1 =  0, 0
    freq0, freq1 = 0, 0
    while True:
        if not program0_done:
            command0 = program[i0]
            parts0 = command0.split()
            if parts0[0]!="rcv":
                i0, freq0 = execute(i0, registers0, program, freq0)
            if parts0[0]=="snd":
                queue0.append(freq0)
            if i0>=len(program):
                program0_done = True
            if parts0[0]=="rcv":
                program0_halted = True
                if queue1:
                    x = parts0[1]
                    registers0[x] = queue1.pop(0)
                    i0+=1
                    program0_halted = False

        if not program1_done:
            command1 = program[i1]
            parts1 = command1.split()
            if parts1[0]!="rcv":
                i1, freq1 = execute(i1, registers1, program, freq1)
            if parts1[0]=="snd":
                queue1.append(freq1)
                res+=1
            if i1>=len(program):
                program1_done = True
            if parts1[0]=="rcv":
                program1_halted = True
                if queue0:
                    x = parts1[1]
                    registers1[x] = queue0.pop(0)
                    i1+=1
                    program1_halted = False
        program0_done = i0>=len(program)
        program1_done = i1>=len(program)

        if program0_halted and program1_halted or program0_halted and program1_done or program0_done and program1_halted or program0_done and program1_done:
            break
    print(res)
        
fname = "day18_input.txt"
with open(fname) as file:
    lines = [line.strip() for line in file]
part1(lines)
part2(lines)