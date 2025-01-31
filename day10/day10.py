def part1(actions, n):
    nums = list(range(n))
    i = 0
    skip_size = 0 
    i, skip_size = do_round(nums, actions, i, skip_size)
    print(nums[0]*nums[1])

def part2(s, n=256):
    hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    nums = list(range(n))
    actions = []
    i, skip_size = 0, 0
    for char in s:
        actions.append(ord(char))
    for x in [17, 31, 73, 47, 23]:
        actions.append(x)
    for _ in range(64):
        i, skip_size = do_round(nums, actions, i, skip_size)
    dense_hash = []
    for i in range(16):
        res = 0
        for j in range(16*i, 16*i+16):
            res^=nums[j]
        dense_hash.append(res)
    res = ""
    for n in dense_hash:
        q, r = divmod(n, 16)
        res+=hex_chars[q]+hex_chars[r]
    return res

def do_round(nums, actions, i, skip_size):
    n = len(nums)
    for x in actions:
        sublist = []
        for j in range(i, i+x):
            sublist.append(nums[j%n])
        sublist = sublist[::-1]
        for j in range(i, i+x):
            nums[j%n] = sublist[j-i]
        i+=x+skip_size
        skip_size+=1
    return i%n, skip_size%n
    
fname, n = "day10_input.txt", 256
#fname, n = "day10_test.txt", 5
with open(fname) as file:
    s = file.read().strip()
    actions = [int(x) for x in s.split(",")]
part1(actions, n)
print(part2(s))
