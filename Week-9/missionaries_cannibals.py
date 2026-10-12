
from collections import deque

start = (3, 3, 0)
goal = (0, 0, 1)

def valid(m, c):
    return (m == 0 or m >= c) and \
           (m == 3 or 3 - m >= 3 - c)

def bfs():
    q = deque([(start, [start])])
    seen = {start}

    while q:
        s, path = q.popleft()
        m, c, b = s

        if s == goal:
            return path

        for x, y in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            if b == 0:
                nm, nc = m - x, c - y
            else:
                nm, nc = m + x, c + y

            nb = 1 - b
            ns = (nm, nc, nb)

            if (0 <= nm <= 3 and 0 <= nc <= 3
                    and valid(nm, nc) and ns not in seen):
                seen.add(ns)
                q.append((ns, path + [ns]))

    return None

path = bfs()

if path:
    for m, c, b in path:
        print(f"m:{m} c:{c} b:{'L' if b == 0 else 'R'}")
else:
    print("No solution found")
