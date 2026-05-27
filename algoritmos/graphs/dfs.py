from typing import Any


def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []

    visited.add(start)
    result.append(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)

    return result


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            for neighbor in reversed[Any](graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4],
}

print("DFS recursivo desde 0:", dfs(graph, 0))
print("DFS iterativo desde 0:", dfs_iterative(graph, 0))
