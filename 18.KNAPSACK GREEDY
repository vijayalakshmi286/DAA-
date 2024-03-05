def knapsack_greedy(values, weights, capacity):
    n = len(values)
    if n != len(weights) or capacity <= 0:
        return "Invalid input"

    value_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]

    value_per_weight.sort(reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []
    rem_cap = capacity

    for vpw, weight, value in value_per_weight:
        if total_weight + weight <= capacity:
            selected_items.append((weight, value))
            total_weight += weight
            total_value += value
            rem_cap = rem_cap - total_weight
        else:
            selected_items.append((weight,value))
            total_weight += weight
            total_value += value
            rem_cap = rem_cap - total_weight
            

    return total_value, selected_items

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
total_value, selected_items = knapsack_greedy(values, weights, capacity)
print("Total value:", total_value)
print("Selected items:", selected_items)
