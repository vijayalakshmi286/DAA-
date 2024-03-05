def knapSack(capacity, wt, val, n): 
    max_values = []
    for item in range(n+1):
        row = []
        for j in range(capacity+1):
            row.append(0)
        max_values.append(row)
 
    for i in range(n + 1):
        for w in range(capacity + 1): 
            if i == 0 or w == 0: 
                max_values[i][w] = 0
            elif wt[i-1] <= w: 
                max_values[i][w] = max(val[i-1] + max_values[i-1][w-wt[i-1]], max_values[i-1][w]) 
            else: 
                max_values[i][w] = max_values[i-1][w]
 
    return max_values[n][capacity] 
 
 
profit = [60, 100, 120]
weight = [10, 20, 30] 
capacity = 50
n = len(profit) 
print(knapSack(capacity, weight, profit, n))
