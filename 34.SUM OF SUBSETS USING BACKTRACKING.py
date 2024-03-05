def subset_sum(set, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False
    if set[n - 1] > sum:
        return subset_sum(set, n - 1, sum)
    return subset_sum(set, n - 1, sum) or subset_sum(set, n - 1, sum - set[n - 1])
set = [1, 2, 3, 4, 5]
n = len(set)
sum = 10
if subset_sum(set, n, sum):
    print("Yes")
else:
    print("No")
