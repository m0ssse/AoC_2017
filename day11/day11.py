def solve(moves):
    furthest = 0
    s, q, r = 0, 0, 0
    directions = {"s": (0, -1, 1), "n": (0, 1, -1), "se": (-1, 0, 1), "nw": (1, 0, -1), "ne": (-1, 1, 0), "sw": (1, -1, 0)}
    for move in moves:
        ds, dq, dr = directions[move]
        s+=ds
        q+=dq
        r+=dr
        furthest = max(furthest, abs(s), abs(q), abs(r))
    print(max(abs(s), abs(q), abs(r)), furthest)


fname = "day11_input.txt"
with open(fname) as file:
    moves = file.read().strip().split(",")
solve(moves)