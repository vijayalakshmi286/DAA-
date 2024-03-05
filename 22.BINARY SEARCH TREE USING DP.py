array = [1,2,3,4,5]
x = int(input())
length = len(array)
low = 0
high = length-1
mid = 0
while low <= high:
    mid = (low + high) // 2
    if array[mid] < x:
        low = mid+1
    elif array[mid] > x:
        high = mid-1
    elif array[mid] == x:
        print(mid)
        break
    else:
        print("not found")
