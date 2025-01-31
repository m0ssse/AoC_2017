def part1(n):
    val = 1
    di, dj = 0, 1
    steps_in_direction = 1
    steps_left = 1
    turns_before_increment = 2
    i, j = 0, 0
    while val<n:
        i+=di
        j+=dj
        val+=1
        steps_left-=1
        if not steps_left:
            di, dj = dj, -di
            turns_before_increment-=1
            if not turns_before_increment:
                steps_in_direction+=1
                turns_before_increment=2
            steps_left = steps_in_direction
    print(abs(i)+abs(j))

def part2(n):
    vals = {(0, 0): 1}
    curr_square = 1
    di, dj = 0, 1
    steps_in_direction = 1
    steps_left = 1
    turns_before_increment = 2
    i, j = 0, 0
    while curr_square<n:
        i+=di
        j+=dj
        curr_square+=1
        steps_left-=1
        newval = 0
        for ii in range(i-1, i+2):
            for jj in range(j-1, j+2):
                if (ii, jj) in vals:
                    newval+=vals[(ii, jj)]
        if newval>n:
            print(newval)
            break
        vals[(i, j)] = newval
        #print(i, j, newval)
        if not steps_left:
            di, dj = dj, -di
            turns_before_increment-=1
            if not turns_before_increment:
                steps_in_direction+=1
                turns_before_increment=2
            steps_left = steps_in_direction
n = 368078
part1(n)
part2(n)