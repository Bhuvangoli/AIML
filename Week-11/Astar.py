import heapq
start = []
goal = []
print("Enter initial state (3x3):")
for i in range(3):
    start.append(list(map(int, input().split())))
print("Enter goal state (3x3):")
for i in range(3):
    goal.append(list(map(int, input().split())))
def heu(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count
def find(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def build(r, c, nr, nc, state):
    newstate = [row[:] for row in state]
    newstate[r][c], newstate[nr][nc] = (
        newstate[nr][nc], newstate[r][c]
    )
    return newstate
def solve(start, goal):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    pq = []
    counter = 0
    start_key = tuple(tuple(row) for row in start)
    goal_key = tuple(tuple(row) for row in goal)
    heapq.heappush(
        pq, (heu(start), 0, counter, start)
    )
    cost = {start_key: 0}
    parent = {start_key: None}
    while pq:
        f, depth, _, state = heapq.heappop(pq)
        key = tuple(tuple(row) for row in state)
        if depth != cost[key]:
            continue
        print("\nCurrent State:")
        for row in state:
            print(row)
        print("Depth cost:", depth)
        if key == goal_key:
            print("\nGoal reached!")
            path = []
            current = key
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("\nSolution Path:")
            for step, s in enumerate(path):
                print("\nStep", step)
                for row in s:
                    print(list(row))
            print("\nTotal moves:", len(path) - 1)
            return
        r0, c0 = find(state)
        for i in range(4):
            nr = r0 + dr[i]
            nc = c0 + dc[i]
            if 0 <= nr < 3 and 0 <= nc < 3:
                newstate = build(
                    r0, c0, nr, nc, state
                )
                newkey = tuple(
                    tuple(row) for row in newstate
                )
                g = depth + 1
                if g < cost.get(newkey, float('inf')):
                    cost[newkey] = g
                    parent[newkey] = key
                    h = heu(newstate)
                    counter += 1
                    heapq.heappush(
                        pq, (g + h, g, counter, newstate)
                    )
    print("\nGoal not reachable!")
if (sorted(sum(start, [])) != list(range(9)) or
    sorted(sum(goal, [])) != list(range(9))):
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
else:
    solve(start, goal)
