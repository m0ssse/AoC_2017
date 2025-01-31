from math import lcm


def part1(scanners):
    res = 0
    for i, (n, c) in scanners.items():
        if i%c==0:
            res+=i*n
    print(res)

def part2(scanners):
    N = 1
    for _, c in scanners.values():
        N = lcm(N, c)
    for k in range(N):
        for i, (_, c) in scanners.items():
            if (i+k)%c==0:
                break
        else:
            print(k)
            break
        
fname = "day13_input.txt"
scanners = {}
with open(fname) as file:
    for line in file:
        i, n = [int(x) for x in line.strip().split(": ")]
        scanners[i] = n, 2*n-2

part1(scanners)
part2(scanners)