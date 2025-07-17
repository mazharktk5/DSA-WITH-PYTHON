

def binarySearch(cards,query):

    start = 0
    end = len(cards)-1

    while start <= end :
        mid = (start + end) // 2
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            end = mid - 1
        elif cards[mid] > query:
            start = mid + 1

    return -1

result = binarySearch([],11)
print(result)