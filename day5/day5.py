def part1(offsets):
    offsets = offsets[:]
    n = 0
    i = 0
    while 0<=i<len(offsets):
        i_new = i+offsets[i]
        offsets[i]+=1
        i=i_new
        n+=1
    print(n)

def part2(offsets):
    offsets = offsets[:]
    n = 0
    i = 0
    while 0<=i<len(offsets):
        i_new = i+offsets[i]
        if offsets[i]>=3:
            offsets[i]-=1
        else:
            offsets[i]+=1
        i=i_new
        n+=1
    print(n)

fname = "day5_input.txt"
with open(fname) as file:
    offsets = [int(x) for x in file]

part1(offsets)
part2(offsets)