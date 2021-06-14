# Knapsack 0/1
# Problem Statement: Given two integer arrays to represent weights and profits of ‘N’ items,
# we need to find a subset of these items which will give us maximum profit such that their
# cumulative weight is not more than a given number ‘W’. Each item can only be selected once,
# which means either we put an item in the knapsack or skip it.

# reference: Aditya Verma Dynamic Programming Playlist
# (https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)

def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits) + 1)]
    n = len(weights)
    result = knapsack_recursive(profits, weights, capacity, n)
    result_memoization = knapsack_memoize(dp, profits, weights, capacity, n)

    print("result recursive approach: ", result)
    print("result memoization: ", result_memoization)
    print("final dp matrix", dp)


def knapsack_recursive(profits, weights, W, n):
    # base checks
    if W == 0 or n == 0:
        return 0

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    if weights[n - 1] <= W:
        return max(profits[n - 1] + knapsack_recursive(
            profits, weights, W - weights[n - 1], n - 1), knapsack_recursive(profits, weights, W, n - 1))

    # recursive call after excluding the element at the currentIndex
    else:
        return knapsack_recursive(profits, weights, W, n - 1)


def knapsack_memoize(dp, profits: list, weights: list, W: int, n: int):
    # base checks
    if W == 0 or n == 0:
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[n][W] != -1:
        return dp[n][W]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    if weights[n - 1] <= W:
        dp[n][W] = max(profits[n - 1] + knapsack_memoize(dp, profits, weights, W - weights[n - 1], n - 1), \
                       knapsack_memoize(dp, profits, weights, W, n - 1))

    # recursive call after excluding the element at the currentIndex
    else:
        dp[n][W] = knapsack_memoize(dp, profits, weights, W, n - 1)

    return dp[n][W]


def knapsack_bottom_up(profits, weights, W):
    # basic checks
    n = len(weights)
    dp = [[0 for x in range(W + 1)] for y in range(n + 1)]

    # process all sub-arrays for all the capacities
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            if weights[i-1] <= j:
                dp[i][j] = max(profits[i-1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])

            else:
                dp[i][j] = dp[i - 1][j]

    # maximum profit will be at the bottom-right corner.
    print("result bottom_up approach", dp[n][W])
    print("DP bottom up: ", dp)


if __name__ == '__main__':
    solve_knapsack([1, 4, 5, 7], [1, 3, 4, 5], 7)
    knapsack_bottom_up([1, 4, 5, 7], [1, 3, 4, 5], 7)
    solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)
    knapsack_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 7)