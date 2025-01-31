def part1(a, b):
    res1 = 0
    N = 40*10**6
    mod2 = 2**16-1
    mod1 = 2**31-1
    a_coeff = 16807
    b_coeff = 48271
    for _ in range(N):
        a = (a*a_coeff)%mod1
        b = (b*b_coeff)%mod1
        res1+=(a&mod2==b&mod2)
    print(res1)

def part2(a, b):
    res = 0
    N = 5*10**6
    mod1 = 2**31-1
    mod2 = 2**16-1
    a_coeff = 16807
    b_coeff = 48271
    for _ in range(N):
        a = (a*a_coeff)%mod1
        while a%4!=0:
            a = (a*a_coeff)%mod1
        b = (b*b_coeff)%mod1
        while b%8!=0:
            b = (b*b_coeff)%mod1
        res+=(a&mod2==b&mod2)
    print(res)

a, b = 722, 354
#a, b = 65, 8921
part1(a, b)
part2(a, b)