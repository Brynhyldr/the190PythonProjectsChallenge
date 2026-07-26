listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]

def findMissingArray(listOfNumbers):
    answer = []
    for i in range(len(listOfNumbers)):
        try:
            if listOfNumbers[i] != listOfNumbers[i+1]-1:
                answer.append(listOfNumbers[i]+1)
        except:
            return answer

print(findMissingArray(listOfNumbers))