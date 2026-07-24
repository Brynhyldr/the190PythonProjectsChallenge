def order(listToOrder):
    orderedList = [listToOrder[0]]
    for i in range(1, len(listToOrder)):
        for j in range(len(orderedList)):
            if listToOrder[i] < orderedList[j]:
                orderedList.insert(j, listToOrder[i])
                break
            elif orderedList[j] == orderedList[len(orderedList)-1]:
                orderedList.append(listToOrder[i])
    return orderedList

def median(orderedList):
    listLength = len(orderedList)
    if listLength % 2 == 0:
        result = (orderedList[round(listLength / 2)] + orderedList[round(listLength / 2 - 1)]) / 2
        print(result)
        return result
    else:
        indexNumber = int((listLength + 1)/2 - 1)
        print(indexNumber)
        return orderedList[indexNumber]

def mean(neededList):
    x = 0
    for i in range(len(neededList)):
        x = x + neededList[i]
    return x/len(neededList)

def mode(neededList):
    token = 0
    intoken = 0
    result = 0
    listLength = len(neededList)
    for i in range(listLength):
        intoken = 0
        for j in range(listLength):
            if neededList[i] == neededList[j]:
                intoken = intoken + 1
        if intoken > token:
            token = intoken
            result = neededList[i]
    return result           