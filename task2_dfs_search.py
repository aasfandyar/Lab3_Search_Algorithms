def dfs(graph, start, goal, visited=None):

    if visited is None:
        visited = set()

    visited.add(start)

    print(start, end=" ")

    if start == goal:
        print("\nGoal Found!")
        return True

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True

    return False


graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A', 'F')
