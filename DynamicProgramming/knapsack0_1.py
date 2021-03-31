# Knapsack 0/1
# Problem Statement: Given two integer arrays to represent weights and profits of ‘N’ items,
# we need to find a subset of these items which will give us maximum profit such that their
# cumulative weight is not more than a given number ‘W’. Each item can only be selected once,
# which means either we put an item in the knapsack or skip it.

# Reference: Educative.io

def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]

    result = knapsack_recursive(profits, weights, capacity, 0)
    result_memoization = knapsack_memoize(dp, profits, weights, capacity, 0)

    print("result recursive approach: ", result)
    print("result memoization: ", result_memoization)
    print("final dp matrix", dp)


def knapsack_recursive(profits, weights, capacity, currentIndex):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(
            profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

    return max(profit1, profit2)


def knapsack_memoize(dp, profits, weights, capacity, currentIndex):

    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_memoize(
            dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_memoize(
        dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]


def knapsack_bottom_up(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # exclude the item
            profit2 = dp[i - 1][c]
            # take maximum
            dp[i][c] = max(profit1, profit2)
    print("DP bottom up: ", dp)
    # maximum profit will be at the bottom-right corner.
    print("result bottom_up approach", dp[n - 1][capacity])


def main():
    solve_knapsack([1, 4, 5, 7], [1, 3, 4, 5], 7)
    knapsack_bottom_up([1, 4, 5, 7], [1, 3, 4, 5], 7)
    solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)
    knapsack_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 7)

main()
