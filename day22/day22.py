def part1(grid, N=10**5):
  n, m = len(grid), len(grid[0)
  di, dj = -1, 0
  infected = set()
  for i in range(n):
    for j in range(m):
      if grid[i][j]=="#":
        infected.add((i, j))
  i, j = n//2, m//2
  res = 0
  for _ in range(N):
    if (i, j) in infected:
      di, dj = dj, -di
      infected.remove((i, j))
    else:
      di, dj = -dj, di
      infected.add((i, j))
      res+=1
    i+=di
    j+=dj
  print(res)

fname = "day22_test.txt"
with open(fname) as file:
  grid = [line.strip() for line in file]
