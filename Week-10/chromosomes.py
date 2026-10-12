
import random

N = 8
POP_SIZE = 10

def fitness(chromosome):
    return chromosome.count('1')

def crossover(p1, p2):
    point = random.randint(1, N - 1)
    return p1[:point] + p2[point:]

def mutate(chromosome):
    i = random.randint(0, N - 1)
    bits = list(chromosome)
    bits[i] = '1' if bits[i] == '0' else '0'
    return ''.join(bits)

population = [
    ''.join(random.choice('01') for _ in range(N))
    for _ in range(POP_SIZE)
]

generation = 0

while True:
    population.sort(key=fitness, reverse=True)

    if fitness(population[0]) == N:
        break

    new_population = population[:2]

    while len(new_population) < POP_SIZE:
        p1, p2 = random.choices(population[:5], k=2)
        child = crossover(p1, p2)

        if random.random() < 0.2:
            child = mutate(child)

        new_population.append(child)

    population = new_population
    generation += 1

print("Best Chromosome:", population[0])
print("Fitness:", fitness(population[0]))
print("Generations:", generation)
