# task1_topological_sort.py

from collections import deque

def topological_sort(graph):

    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque()

    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order


graph = {
    0: [1,3],
    1: [2,3],
    2: [4,5],
    3: [4],
    4: [5],
    5: []
}

print("Topological Sort:", topological_sort(graph))
