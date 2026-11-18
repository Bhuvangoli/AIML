def alpha_beta(node, depth, max_depth, maximizing,
               values, alpha, beta, pruned):
    if depth == max_depth:
        return values[node]
    if maximizing:
        best = float('-inf')
        for i in range(2):
            child = node * 2 + i
            val = alpha_beta(
                child, depth + 1, max_depth,
                False, values, alpha, beta, pruned
            )
            best = max(best, val)
            alpha = max(alpha, best)
            if alpha >= beta:
                # Record all remaining leaves in skipped subtree
                next_child = child + 1
                remaining_depth = max_depth - depth - 1
                start = next_child * (2 ** remaining_depth)
                end = (node + 1) * (2 ** (max_depth - depth))
                pruned.extend(range(start, end))
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            child = node * 2 + i
            val = alpha_beta(
                child, depth + 1, max_depth,
                True, values, alpha, beta, pruned
            )
            best = min(best, val)
            beta = min(beta, best)
            if alpha >= beta:
                next_child = child + 1
                remaining_depth = max_depth - depth - 1
                start = next_child * (2 ** remaining_depth)
                end = (node + 1) * (2 ** (max_depth - depth))
                pruned.extend(range(start, end))
                break
        return best
n = int(input("Enter number of leaf nodes: "))
if n < 2 or (n & (n - 1)) != 0:
    print("Number of leaf nodes must be a power of 2.")
else:
    values = list(map(int, input(
        "Enter leaf node values: "
    ).split()))
    if len(values) != n:
        print("Invalid number of values!")
    else:
        max_depth = n.bit_length() - 1
        pruned = []
        result = alpha_beta(
            0, 0, max_depth, True,
            values, float('-inf'),
            float('inf'), pruned
        )
        print("\n--- Alpha-Beta Pruning Result ---")
        print("Leaf Nodes:", values)
        print("\nPruned Nodes:")
        if pruned:
            for i in sorted(set(pruned)):
                print(f"Leaf {i + 1}: {values[i]}")
        else:
            print("No nodes pruned")
        print("\nFinal Optimal Value:", result)