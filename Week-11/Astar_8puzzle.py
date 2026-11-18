import heapq
class PuzzleState:
    def __init__(self, board, g=0, parent=None):
        self.board = board  # 1D tuple of length 9 representing the 3x3 board
        self.g = g          # Cost from start to current node
        self.parent = parent
        self.h = self.calculate_manhattan_distance()
        self.f = self.g + self.h

    def calculate_manhattan_distance(self):
        distance = 0
        goal_positions = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 0: (2, 2)  # 0 represents the empty space
        }
        for i, val in enumerate(self.board):
            if val != 0:
                current_row, current_col = i // 3, i % 3
                goal_row, goal_col = goal_positions[val]
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def get_neighbors(self):
        neighbors = []
        zero_idx = self.board.index(0)
        row, col = zero_idx // 3, zero_idx % 3

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero_idx = new_row * 3 + new_col
                new_board = list(self.board)
                new_board[zero_idx], new_board[new_zero_idx] = new_board[new_zero_idx], new_board[zero_idx]
                neighbors.append(PuzzleState(tuple(new_board), self.g + 1, self))
        return neighbors

    def __lt__(self, other):
        return self.f < other.f

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()

def solve_8_puzzle(start_board):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    start_state = PuzzleState(start_board)

    open_set = []
    heapq.heappush(open_set, start_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.board == goal:
            path = []
            curr = current_state
            while curr:
                path.append(curr)
                curr = curr.parent
            return path[::-1]

        closed_set.add(current_state.board)

        for neighbor in current_state.get_neighbors():
            if neighbor.board in closed_set:
                continue

            heapq.heappush(open_set, neighbor)

    return None

initial_state = (1, 3, 0, 4, 2, 6, 7, 5, 8)

print("Searching for a solution...")
solution_path = solve_8_puzzle(initial_state)

if solution_path:
    print(f"Solution found in {len(solution_path) - 1} moves!\\n")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        state.print_board()
else:
    print("No solution exists.")