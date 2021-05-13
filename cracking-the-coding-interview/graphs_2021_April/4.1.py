def check_path_aux2(a, b, graph, visited):
    if a == b:
        return True
    visited.add(a)
    print(a, end=" ")
    for node in graph[a]:
        if node not in visited:
            if check_path_aux2(node, b, graph, visited):
                return True

graph = {
    1: [2, 3, 4],
    2: [1],
    3: [6, 1],
    4: [5, 1],
    5: [7, 8, 4],
    6: [3],
    7: [5],
    8: [5],
    9: []
}

print(check_path_aux2(3, 2, graph, set()))