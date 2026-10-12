
from math import gcd

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if (target > max(jug1, jug2) or
        target % gcd(jug1, jug2) != 0):
    print("No solution possible")
else:
    a = 0
    b = 0
    steps = [(a, b)]

    while (a != target or b != 0) and \
          (a != 0 or b != target):

        if a == 0:
            a = jug1
        elif b == jug2:
            b = 0
        else:
            amount = min(a, jug2 - b)
            a -= amount
            b += amount

        steps.append((a, b))

    print("\nSteps:")
    for i in range(len(steps)):
        print("Step", i, ":", steps[i])

    print("\nFinal State:")
    print("Jug 1 =", a)
    print("Jug 2 =", b)
