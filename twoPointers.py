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
