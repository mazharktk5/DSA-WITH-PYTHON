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

def factorial(n):
    if n == 0 or n == 1:
        print(f"the factorial of {n} is :", {n})
        return 1
    else:

        result = n * factorial(n-1)
        print(f"the factorial of {n} is :",{result})
        return result
    
factorial(5)

    
    