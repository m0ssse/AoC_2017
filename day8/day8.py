def solve(lines):
    registers = {}
    best = 0
    for line in lines:
        target, action, amount, _, val1, op, val2 = line.split()
        if target not in registers:
            registers[target] = 0
        if val1 not in registers:
            registers[val1] = 0
        val1 = registers[val1]
        cond = eval(f"{val1} {op} {val2}")
        if cond:
            if action == "inc":
                registers[target]+=int(amount)
            else:
                registers[target]-=int(amount)
            best = max(best, registers[target])
    print(max(registers.values()), best)
        

fname = "day8_input.txt"
with open(fname) as file:
    lines = [line.strip() for line in file]
solve(lines)