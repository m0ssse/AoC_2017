def part1(moves, s):
    s = list(s)
    for move in moves:
        if move[0]=="s":
            spin(s, int(move[1:]))
        elif move[0]=="x":
            i, j = [int(x) for x in move[1:].split("/")]
            exchange(s, i, j)
        else:
            a, b = move[1], move[-1]
            partner(s, a, b)
    return "".join(s)

def part2(moves, s):
    seen = {}
    for i in range(10**9):
        if s in seen:
            break
        seen[s]=i
        s = part1(moves, s)
    c = i-seen[s]
    rem = (10**9-i)%c
    for _ in range(rem):
        s = part1(moves, s)
    print(s)

        
    

def spin(program, n):
    n = n%16
    for _ in range(n):
        program.insert(0, program.pop())

def exchange(program, i, j):
    program[i], program[j] = program[j], program[i]

def partner(program, a, b):
    i, j = program.index(a), program.index(b)
    program[i], program[j] = program[j], program[i]

fname, s = "day16_input.txt", "abcdefghijklmnop"
#fname, n = "day16_test.txt", "abcde"
with open(fname) as file:
    moves = file.read().strip().split(",")

print(part1(moves, s))
part2(moves, s)