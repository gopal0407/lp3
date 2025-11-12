def knapsack_01_dp(values, weights, capacity):
    """
    Solves the 0-1 Knapsack problem using dynamic programming.
    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    """
    n = len(values)
    # Create DP table with dimensions (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include item i-1
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Exclude item i-1
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    capacity = int(input("Enter knapsack capacity: "))

    values = []
    weights = []

    for i in range(n):
        val = int(input(f"Enter value of item {i+1}: "))
        wt = int(input(f"Enter weight of item {i+1}: "))
        values.append(val)
        weights.append(wt)

    max_value = knapsack_01_dp(values, weights, capacity)
    print(f"\n💰 Maximum value in knapsack = {max_value}")





   
