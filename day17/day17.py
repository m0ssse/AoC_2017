class ListNode:
    def __init__(self, n):
        self.val = n
        self.next = None

def part1(step_size):
    buffer = [0]
    i=0
    for n in range(1, 2018):
        i = (i+step_size)%n
        buffer.insert(i+1, n)
        i+=1
    print(buffer[i+1])

def part2(step_size):
    value_after_0 = 0
    i = 0
    N = 50*10**6
    for n in range(1, N+1):
        i = (i+step_size)%n
        if i==0:
           value_after_0 = n
        i+=1
    print(value_after_0)

part1(356)
part2(356)