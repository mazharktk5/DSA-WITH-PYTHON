

def maxSum(arr, k):
    max_sum = current_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum


print(maxSum([1, 3, 2, 5, 6, 8], 3))
