n = int(input("Items: "))
w = int(input("Capacity: "))
val, wt = [], []
for i in range(n):
    val.append(int(input(f"Value {i+1}: ")))
    wt.append(int(input(f"Weight {i+1}: ")))

dp = [[0]*(w+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, w+1):
        if wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print("Max value:", dp[n][w])
