def solve(grid):
    n, m = len(grid), len(grid[0])
    i = 0
    steps = 0
    for j, char in enumerate(grid[0]):
        if char=="|":
            break
    di, dj = 1, 0
    res=""
    while True:
        if i<0 or i>=n or j<0 or j>=m or grid[i][j]==" ":
            break
        steps+=1
        char = grid[i][j]
        if char in "|-":
            pass
        elif char=="+":
            for ddi, ddj in [(dj, -di), (-dj, di)]:
                ii, jj = i+ddi, j+ddj
                if ii<0 or ii>=n or jj<0 or jj>=m or grid[ii][jj]==" ":
                    continue
                di, dj = ddi, ddj
        else:
            res+=char
        i+=di
        j+=dj
    print(res, steps)


fname = "day19_input.txt"
with open(fname) as file:
    grid = [line.strip("\n") for line in file]
solve(grid)