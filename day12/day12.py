def solve(lines):
    graph = {}
    for line in lines:
        parts = line.split(" <-> ")
        node = parts[0]
        if node not in graph:
            graph[node] = set()
        if len(parts)==2:
            neighbs = parts[1].split(", ")
            for neighb in neighbs:
                if neighb not in graph:
                    graph[neighb] = set()
                graph[node].add(neighb)
                graph[neighb].add(node)
    components = {}
    visited = set()
    for node in graph:
        if node not in visited:
            components[node] = set()
            dfs(node, graph, visited, node, components)
    #print(components)
    for node, component in components.items():
        if "0" in component:
            print(len(component), len(components))
            break
    

def dfs(node, graph, visited, source, components):
    visited.add(node)
    components[source].add(node)
    for neighb in graph[node]:
        if neighb in visited:
            continue
        visited.add(neighb)
        dfs(neighb, graph, visited, source, components)

fname = "day12_input.txt"
with open(fname) as file:
    lines = [line.strip() for line in file]
solve(lines)