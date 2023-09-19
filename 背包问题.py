def zero_one_package(values, costs, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(values)):
        for j in range(capacity, 0, -1):
            if j >= costs[i]:
                dp[j] = max(dp[j], dp[j - costs[i]] + values[i])
    return dp[capacity]


values = [2, 4, 4, 5]
costs = [1, 2, 3, 4]
capacity = 5
print(zero_one_package(values, costs, capacity))


def complete_package(values, costs, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(values)):
        for j in range(1, capacity + 1):
            if j >= costs[i]:
                dp[j] = max(dp[j], dp[j - costs[i]] + values[i])
    return dp[capacity]


values = [2, 4, 4, 5]
costs = [1, 2, 3, 4]
capacity = 5
print(complete_package(values, costs, capacity))
