def part1(memory):
    seen = {}
    k = 0
    while True:
        config = tuple(memory)   
        if config in seen:
            print(len(seen))
            print(k-seen[config])
            break
        seen[config] = k
        n, i = max((val, -ind) for ind, val in enumerate(memory))
        i*=-1
        memory[i] = 0
        #print(f"max value at index {i}: {n}")
        ii=i+1
        while n:
            memory[ii%len(memory)]+=1
            n-=1
            ii+=1
        #print(f"memory is now {memory}")
        k+=1

fname = "day6_test.txt"
with open(fname) as file:
    memory = [int(x) for x in file.read().split()]

part1(memory)