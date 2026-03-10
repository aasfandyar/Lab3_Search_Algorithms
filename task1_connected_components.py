from collections import deque

def bfs(graph, start, visited):

    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def count_components(graph):

    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)
            count += 1

    return count


graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}

print("Connected Components:", count_components(graph))
