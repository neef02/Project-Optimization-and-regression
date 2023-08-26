class CargoItem:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def approximate_knapsack(items, capacity):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    knapsack = []
    total_weight = 0
    total_value = 0

    for item in items:
        if total_weight + item.weight <= capacity:
            knapsack.append(1)
            total_weight += item.weight
            total_value += item.value
        else:
            knapsack.append(0)
            break  # Stop adding items if capacity is reached

    return knapsack, total_value


def exact_knapsack(items, capacity):
    n = len(items)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1].weight <= w:
                table[i][w] = max(items[i - 1].value + table[i - 1][w - items[i - 1].weight], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    knapsack = []
    total_value = table[n][capacity]

    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            knapsack.append(1)
            w -= items[i - 1].weight
        else:
            knapsack.append(0)

    knapsack.reverse()
    return knapsack, total_value


# P01 dataset
weights = [25,
35,
45,
 5,
25,
 3,
 2,
 2]
profits = [350,
400,
450,
 20,
 70,
  8,
  5,
  5]


items = [CargoItem(weight, profit) for weight, profit in zip(weights, profits)]
capacity = 104

# Approximate Algorithm
approx_knapsack, approx_total_value = approximate_knapsack(items, capacity)
print("Approximate Knapsack:", approx_knapsack)
print("Approximate Total Value:", approx_total_value)

# Exact Algorithm
exact_knapsack, exact_total_value = exact_knapsack(items, capacity)
print("Exact Knapsack:", exact_knapsack)
print("Exact Total Value:", exact_total_value)

approx_percentage = (approx_total_value/exact_total_value ) * 100
print("Approximate Solution Quality: {:.2f}%".format(approx_percentage))
