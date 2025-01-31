def part1(lines):
    for s in lines:
        print(get_score(s))

def part2(lines):
    for s in lines:
        print(count_garbage(s))

def get_score(s):
    total = 0
    i = 0
    curr_score = 0
    garbage = False
    while i<len(s):
        char = s[i]
        i+=1
        if garbage and char=="!":
            i+=1
        elif garbage and char==">":
            garbage = False
        elif not garbage and char=="{":
            curr_score+=1
        elif not garbage and char=="<":
            garbage = True
        elif not garbage and char=="}":
            total+=curr_score
            curr_score-=1
    return total

def count_garbage(s):
    res = 0
    i = 0
    garbage = False
    while i<len(s):
        char = s[i]
        i+=1
        if not garbage and char=="<":
            garbage = True
        elif garbage and char=="!":
            i+=1
        elif garbage and char==">":
            garbage = False
        elif garbage:
            res+=1
    return res



fname = "day9_input.txt"
with open(fname) as file:
    lines = [line.strip() for line in file]

part1(lines)
part2(lines)