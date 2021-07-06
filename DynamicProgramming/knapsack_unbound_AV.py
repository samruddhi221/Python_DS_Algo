# Given two integer arrays to represent weights and profits of ‘N’ items,
# we need to find a subset of these items which will give us maximum profit
# such that their cumulative weight is not more than a given number ‘W’.
# We can assume an infinite supply of item quantities; therefore,
# each item can be selected multiple times.

def solve_knapsack_unbound(profits, weights, capacity):
    # TODO: Write your code here
    return -1


if __name__ == '__main__':
    print(solve_knapsack_unbound([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_knapsack_unbound([15, 50, 60, 90], [1, 3, 4, 5], 6))

