def part1(particles):
    for _ in range(10000):
        for i, particle in enumerate(particles):
            particles[i] = move(particle)
    best = particles[0]
    mindist = float("inf")
    res = 0
    for i, (pos, _, _) in enumerate(particles):
        dist = sum(abs(x) for x in pos)
        if dist<mindist:
            mindist = dist
            res = i
    print(res)


def move(particle):
    (ax, ay, az), (vx, vy, vz), (x, y, z) = particle
    vx, vy, vz = vx+ax, vy+ay, vz+az
    x, y, z = x+vx, y+vy, z+vz
    return (ax, ay, az), (vx, vy, vz), (x, y, z)


particles = []
fname = "day20_input.txt"
with open(fname) as file:
    for line in file:
        pos, v, a = line.strip().split(", ")
        pos = [int(x) for x in pos[3:-1].split(",")]
        v = [int(x) for x in v[3:-1].split(",")]
        a = [int(x) for x in a[3:-1].split(",")]
        particles.append((pos, v, a))
part1(particles)