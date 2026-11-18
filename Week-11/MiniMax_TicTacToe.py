import math
import copy

def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---|---|---")
    print()

def check_winner(board):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for win in win_states:
        if board[win[0]] == board[win[1]] == board[win[2]] and board[win[0]] != ' ':
            return board[win[0]]
    if ' ' not in board:
        return 'Tie'
    return None

def minimax(board, depth, is_maximizing, ai_player, opponent):
    winner = check_winner(board)
    if winner == ai_player:
        return 10 - depth
    if winner == opponent:
        return depth - 10
    if winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_player
                score = minimax(board, depth + 1, False, ai_player, opponent)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = opponent
                score = minimax(board, depth + 1, True, ai_player, opponent)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def get_next_best_state(current_state, player):
    if len(current_state) != 9:
        raise ValueError("The board state must contain exactly 9 elements.")

    if check_winner(current_state) is not None:
        print("Game is already over!")
        return current_state

    opponent = 'O' if player == 'X' else 'X'
    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if current_state[i] == ' ':
            current_state[i] = player
            score = minimax(current_state, 0, False, player, opponent)
            current_state[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    if best_move != -1:
        next_state = copy.deepcopy(current_state)
        next_state[best_move] = player
        return next_state

    return current_state

start_state_1 = [
    'X', 'X', ' ',
    ' ', 'O', ' ',
    ' ', ' ', ' '
]

print("Start State:")
print_board(start_state_1)

next_state_1 = get_next_best_state(start_state_1, player='O')
print("Next Best State for Player 'O':")
print_board(next_state_1)