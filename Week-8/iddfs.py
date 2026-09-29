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


def depth_limited_search(start, goal, limit):

    open_list = [(start, 0)]
    closed_list = []
    parent = {start: None}

    while open_list:

        node, depth = open_list.pop()

        if node in closed_list:
            continue

        closed_list.append(node)

        print("OPEN:", open_list)
        print("CLOSED:", closed_list)

        if node == goal:

            path = []
            current = node

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path, open_list, closed_list

        if depth < limit:

            for neighbour in reversed(graph[node]):

                if neighbour not in closed_list:
                    parent[neighbour] = node
                    open_list.append((neighbour, depth + 1))

    return None, open_list, closed_list


depth = 0

while True:

    print("\n==============================")
    print("DEPTH LIMIT:", depth)
    print("==============================")

    path, open_list, closed_list = depth_limited_search(
        start,
        goal,
        depth
    )

    if path is not None:
        print("\nGoal Found!")
        print("Path:", " -> ".join(path))
        print("Final OPEN:", open_list)
        print("Final CLOSED:", closed_list)
        break

    depth += 1