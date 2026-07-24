import math

list1 = [5, 2, 7, 3, 9]

def order(listToOrder):
    orderedList = [listToOrder[0]]
    for i in range(len(listToOrder)):
        for j in range(len(orderedList)):
            if listToOrder[i] < orderedList[j]:
                orderedList.insert(j, listToOrder[i])
                break
    return orderedList

list2 = order(list1)

for i in list2:
    print(i)