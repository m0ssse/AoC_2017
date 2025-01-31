def part1(lines):
    res = 0
    for line in lines:
        res+=max(line)-min(line)
    print(res)

def part2(lines):
    print(sum(helper(line) for line in lines))

def helper(line):
    for i in range(len(line)):
        for j in range(len(line)):
            if i==j:
                continue
            if line[i]%line[j]==0:
                return line[i]//line[j]

fname = "day2_input.txt"
with open(fname) as file:
    lines = [[int(x) for x in line.strip().split()] for line in file]
part1(lines)
part2(lines)