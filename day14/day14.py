def solve(s):
    hex_to_bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "a": "1010", "b": "1011", "c": "1100", "d": "1101", "e": "1110", "f": "1111"}
    res1 = 0
    res2 = 0
    n, m = 128, 128
    grid = []
    visited = set()
    for i in range(128):
        key = f"{s}-{i}"
        hash = knot_hash(key)
        hash = "".join(hex_to_bin[c] for c in hash)
        grid.append(hash)
        res1+=hash.count("1")
    print(res1)
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="1" and (i, j) not in visited:
                res2+=1
                dfs(grid, i, j, n, m, visited)
    print(res2)


def knot_hash(s, n=256):
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

def dfs(grid, i, j, n, m, visited):
    visited.add((i, j))
    for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if ii<0 or ii>=n or jj<0 or jj>=m or (ii, jj) in visited or grid[ii][jj]=="0":
            continue
        visited.add((ii, jj))
        dfs(grid, ii, jj, n, m, visited)

fname = "day14_input.txt"
with open(fname) as file:
    s = file.read().strip()
solve(s)