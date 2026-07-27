inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

def groupSameIndices(inputList):
    answer = []
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            try:
                answer[j].append(inputList[i][j])
            except IndexError:
                answer.append([])
                answer[j].append(inputList[i][j])
    return answer

print(groupSameIndices(inputLists))