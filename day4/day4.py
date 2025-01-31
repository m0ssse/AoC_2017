def part1(lines):
    res1 = sum(check_line(line) for line in lines)
    res2 = sum(check_line2(line) for line in lines)
    print(res1, res2)

def check_line(lines):
    seen = set()
    for word in lines:
        if word in seen:
            return False
        seen.add(word)
    return True

def check_line2(lines):
    seen = set()
    for word in lines:
        word = "".join(sorted(word))
        if word in seen:
            return False
        seen.add(word)
    return True

fname = "day4_input.txt"
with open(fname) as file:
    phrases = [line.strip().split() for line in file]
part1(phrases)