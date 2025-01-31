def solve(programs):
    parents = {}
    weights = {}
    children = {}
    weight_sums = {}
    for line in programs:
        parts = line.split(" -> ")
        node, weight = parts[0].split(" (")
        weight = int(weight[:-1])
        weights[node] = weight
        children[node] = []
        if len(parts)==2:
            asd = parts[1].split(", ")
            for child in asd:
                parents[child] = node
                children[node].append(child)
    for node in weights:
        if node not in parents:
            print(node)
            root = node
            break
    calculate_tower_weights(root, weights, children, weight_sums)
    curr_node = root
    while not is_balanced(curr_node, weight_sums, children):
        child_weight_sums = {}
        for child in children[curr_node]:
            w = weight_sums[child]
            if w not in child_weight_sums:
                child_weight_sums[w] = []
            child_weight_sums[w].append(child)
        for w, child_list in child_weight_sums.items():
            if len(child_list)==1:
                curr_node = child_list[0]
                wrong_w = w
            else:
                target_w = w
    print(weights[curr_node]+target_w-wrong_w)

                


def is_balanced(node, weight_sums, children):
    return len(set((weight_sums[child]) for child in children[node]))==1

def calculate_tower_weights(node, weights, children, res):
    if node in res:
        return res[node]
    total = weights[node]
    for child in children[node]:
        total+=calculate_tower_weights(child, weights, children, res)
    res[node] = total
    return total


fname = "day7_input.txt"
with open(fname) as file:
    lines = [line.strip() for line in file]
solve(lines)