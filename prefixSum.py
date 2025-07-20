

def prefixSum(arr):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]

    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix



arr = [2,5,3,1,7,8]
print(prefixSum(arr))
print(max(prefixSum(arr)))