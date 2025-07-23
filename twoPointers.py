def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return True
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return False


arr = [1, 3, 4, 5, 7, 10, 12]
print(has_pair_with_sum(arr, 20))  

# arr = [2, 4, 6, 8, 9, 11, 15]
# target = 17

Loop 1: arr[left] + arr[right] = 13
curr_sum = 13 → move right

Loop 2: arr[left] + arr[right] = 15
curr_sum = 15 → move right

Loop 3: arr[left] + arr[right] = 16
curr_sum = 16 → move right

Loop 4: arr[left] + arr[right] = 17
curr_sum = 17 → return true
