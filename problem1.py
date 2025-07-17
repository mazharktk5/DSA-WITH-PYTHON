
def locate_card(cards,query):
    position = 0

    while True:
        if cards[position] == query:
            return position
        position += 1

        if position == len(cards):
            return -1
        


cards = [78,34,23,11,8]
query = 23
print(locate_card(cards,query))  