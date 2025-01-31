def part1(nums):
    res1 = 0
    res2 = 0
    n=len(nums)
    step = n//2
    for i, x in enumerate(nums):
        if x==nums[i-1]:
            res1+=x
        if x==nums[(i+step)%n]:
            res2+=x
    print(res1, res2)

fname = "day1_input.txt"
with open(fname) as file:
    nums = [int(x) for x in file.read()]

part1(nums)