def part1(particles):
    helper = []
    for i, particle in enumerate(particles):
        helper.append((get_manhattan(particle), i))
    helper.sort()
    print(helper[0])

def part2(particles):
    collisions_by_time = {}
    for i in range(len(particles)):
        for j in range(i):
            p1, p2 = particles[i], particles[j]
            for t in get_collision_time(p1, p2):
                if t>=0:
                    if t not in collisions_by_time:
                        collisions_by_time[t] = set()
                    collisions_by_time[t].add((i, j))
    collisions = sorted((t, particles) for t, particles in collisions_by_time.items())
    collided_particles = set()
    for t, pairs in collisions:
        colliding = set()
        for i, j in pairs:
            if i in collided_particles or j in collided_particles:
                continue
            colliding.add(i)
            colliding.add(j)
        for i in colliding:
            collided_particles.add(i)
    print(len(particles)-len(collided_particles))
          
def get_pos(particle, t):
    (ax, ay, az), (vx, vy, vz), (x, y, z) = particle
    k = (t*(t+1))//2
    return x+t*vx+k*ax, y+t*vy+k*ay, z+t*vz+k*az

def get_manhattan(particle):
    (ax, ay, az), (vx, vy, vz), (x, y, z) = particle
    a = abs(ax)+abs(ay)+abs(az)
    v = abs(vx)+abs(vy)+abs(vz)
    p = abs(x)+abs(y)+abs(z)
    return a, v, p

def sqrt_binary(n):
    L, R = 0, n
    while L<R:
        M = (L+R)//2
        if M**2==n:
            return M
        elif M**2>n:
            R=M
        else:
            L=M+1
    return L

def solve_quadratic_eq(a, b, c):
    #print(a, b, c)
    if a==0:
        if b!=0 and c%b==0:
            return [-c//b]
        elif c==0:
            return [0]
        return []
    D = b**2-4*a*c
    #print(D)
    d = sqrt_binary(D)
    if d**2!=D:
        return []
    options = []
    num1 = -b+d
    num2 = -b-d
    if num1%(2*a)==0:
        options.append(num1//(2*a))
    if num2%(2*a)==0:
        options.append(num2//(2*a))
    return options

def get_collision_time(p1, p2):
    (a1, _, _), (v1, _, _), (x1, _, _) = p1
    (a2, _, _), (v2, _, _), (x2, _, _) = p2
    da = (a2-a1)
    dv = 2*(v2-v1)
    dx = 2*(x2-x1)
    collision_times =  solve_quadratic_eq(da, da+dv, dx)
    return [t for t in collision_times if get_pos(p1, t)==get_pos(p2, t)]

particles = []
fname = "day20_input.txt"
with open(fname) as file:
    for line in file:
        pos, v, a = line.strip().split(", ")
        pos = tuple([int(x) for x in pos[3:-1].split(",")])
        v = tuple([int(x) for x in v[3:-1].split(",")])
        a = tuple([int(x) for x in a[3:-1].split(",")])
        particles.append((a, v, pos))
part1(particles)
part2(particles)