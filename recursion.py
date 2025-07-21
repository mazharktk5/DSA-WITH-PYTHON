# def countDown(n):
#     if n == 0:
#         return "Blast off!"
#     else:
#         print(n)
#         return countDown(n-1)

# countDown(6)


# def countUp(current,n):
#     if current > n:
#         return "reached"
#     else:
#         print(current)
#         return countUp(current+1,n)

# countUp(1,6)


# sum of n natural numbers

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)

# print(sum(5))


# factorail

# def factorial(n):
#     if n == 0 or n == 1:
#         print(f"the factorial of {n} is :", {n})
#         return 1
#     else:

#         result = n * factorial(n-1)
#         print(f"the factorial of {n} is :",{result})
#         return result

# factorial(5)

# def sum(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum(arr[1:])
# arr = [1,2,3,4]
# print(sum(arr))


# def reverse_array(arr):
#     if len(arr) == 0:
#         return []
#     last = arr[-1]
#     rest_reversed = reverse_array(arr[:-1])
#     return [last] + rest_reversed

# arr = [1,2,3,4,5]
# print(reverse_array(arr))

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(6))


# def linearSearch(arr,start,target):
#     if start < 0:
#         return -1
#     if arr[start] == target:
#         return start
#     else:
#         return linearSearch(arr,start-1,target)

# arr = [1,4,5,6,7,8]
# print(linearSearch(arr,5,7))


# def isSorted(arr,i):
#     if i == len(arr)-1:
#         return True
#     if arr[i] > arr[i + 1]:
#         print(f"array is not sorted because {arr[i]} is greater then {arr[i+1]}")
#         return
#     else:

#         return isSorted(arr,i+1)


# print("array is sorted")
# print(isSorted([1,2,3,4],0))

# def reverseStr(str):
#     if len(str) == 0:
#         return ""
#     else:
#         return reverseStr(str[1:]) + str[0]

# str = "mazhar"
# print(reverseStr(str))












# def longest_subarray_sum_k(nums, k):
#     prefix_sum = 0
#     max_len = 0
#     seen = {0: -1} 

#     print(f"Target sum = {k}")
#     for i, num in enumerate(nums):
#         prefix_sum += num
#         print(f"\nIndex: {i}, Num: {num}, Prefix Sum: {prefix_sum}")

#         if prefix_sum - k in seen:
#             length = i - seen[prefix_sum - k]
#             max_len = max(max_len, length)
#             print(f" Found subarray [{seen[prefix_sum - k] + 1}:{i}] with sum = {k}, length = {length}")

        
#         if prefix_sum not in seen:
#             seen[prefix_sum] = i
#             print(f" Storing prefix_sum {prefix_sum} at index {i}")

#     print(f"\n Longest subarray length with sum {k} = {max_len}")
#     return max_len


# print(longest_subarray_sum_k([1, 2, 3, 4,5, 6, 7, 8, 9], 13))
