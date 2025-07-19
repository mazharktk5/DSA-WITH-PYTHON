def countDown(n):
    if n == 0:
        return "Blast off!"
    else:
        print(n)
        return countDown(n-1)
    
countDown(6)