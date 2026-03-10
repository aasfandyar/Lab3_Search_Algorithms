from collections import deque

capacity = (4, 3)
target = 2

visited = set()

def dfs(state):

    x, y = state

    if state in visited:
        return False

    visited.add(state)

    print(state)

    if x == target:
        print("Goal Reached:", state)
        return True

    possible_states = [

        (capacity[0], y),   # fill 4
        (x, capacity[1]),   # fill 3
        (0, y),             # empty 4
        (x, 0),             # empty 3

        (x - min(x, capacity[1]-y),
         y + min(x, capacity[1]-y)),

        (x + min(y, capacity[0]-x),
         y - min(y, capacity[0]-x))
    ]

    for new_state in possible_states:
        if dfs(new_state):
            return True

    return False


dfs((0,0))
