def min_max(arr):
    if len(arr) == 1:
        return arr[0],arr[0]
    elif len(arr) == 2:
        return (arr[0],arr[1]) if arr[0] < arr[1] else (arr[1],arr[0])
    mid = len(arr) // 2
    left_min, left_max = min_max(arr[:mid])
    right_min , right_max = min_max(arr[mid:])
    min_val = min(left_min , right_min)
    max_val = max(left_max , right_max)
    return min_val,max_val
arr = [4,3,5,6,8]
min_val , max_val = min_max(arr)
print(min_val,max_val)
