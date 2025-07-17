
# def locate_card(cards,query):
#     position = 0

#     while True:
#         if cards[position] == query:
#             return position
#         position += 1

#         if position == len(cards):
#             return -1
        


# cards = [78,34,23,11,8]
# query = 23
# print(locate_card(cards,query))  


# def locate_card(cards, query):
#     position = 0

#     while position < len(cards):
#         if cards[position] == query:
#             return position
#         position += 1

#     return -1
# cards = []
# query = 0
# print(locate_card(cards,query))


def locate_card(cards, query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            print(f" Found at position {position}")
            return position
        position += 1

    print("Number does not exist in the list.")
    return -1


cards = [78, 34, 23, 11, 8]
query = 23

position = locate_card(cards, query)
