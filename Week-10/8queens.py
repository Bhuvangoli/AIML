import random

N = 8
POP_SIZE = 100

def fitness(board):
    score = 0

    for i in range(N):
        for j in range(i + 1, N):
            if abs(board[i] - board[j]) != abs(i - j):
                score += 1

    return score

def crossover(p1, p2):
    point = random.randint(1, N - 1)
    child = p1[:point]
    child += [x for x in p2 if x not in child]
    return child

def mutate(board):
    board = board[:]
    i, j = random.sample(range(N), 2)
    board[i], board[j] = board[j], board[i]
    return board

def print_board(board):
    for row in range(N):
        for col in range(N):
            print("Q" if board[col] == row else ".", end=" ")
        print()

population = [
    random.sample(range(N), N)
    for _ in range(POP_SIZE)
]

generation = 0

while True:
    population.sort(key=fitness, reverse=True)
    best = population[0]

    if fitness(best) == 28:
        break

    new_population = population[:2]

    while len(new_population) < POP_SIZE:
        p1, p2 = random.choices(population[:20], k=2)
        child = crossover(p1, p2)

        if random.random() < 0.2:
            child = mutate(child)

        new_population.append(child)

    population = new_population
    generation += 1

print("Solution:", best)
print("Fitness Score:", fitness(best))
print("Generations:", generation)
print("\nChessboard:")
print_board(best)
