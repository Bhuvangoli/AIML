from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

open_list = deque([start])
closed_list = []
parent = {start: None}

while open_list:
    node = open_list.popleft()

    if node in closed_list:
        continue

    closed_list.append(node)

    print("OPEN:", list(open_list))
    print("CLOSED:", closed_list)

    if node == goal:
        break

    for neighbour in graph[node]:
        if neighbour not in closed_list and neighbour not in open_list:
            parent[neighbour] = node
            open_list.append(neighbour)

path = []

if goal in closed_list:
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

print("\nPath:", " -> ".join(path))
print("Final OPEN:", list(open_list))
print("Final CLOSED:", closed_list)