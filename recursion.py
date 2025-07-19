# def countDown(n):
#     if n == 0:
#         return "Blast off!"
#     else:
#         print(n)
#         return countDown(n-1)
    
# countDown(6)


def countUp(current,n):
    if current > n:
        return "reached"
    else:
        print(current)
        return countUp(current+1,n)

countUp(1,6)