

list = [1,3,5,7,8]

list.insert(0,2)
print(list)
list.insert(2,9)
print(list)
list.insert(len(list),10)
print(list)

list.remove(8)
print(list)
del list[0]
print(list)

for i in range(len(list)):
    print(list[i])
