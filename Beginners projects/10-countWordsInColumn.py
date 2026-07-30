import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding = 'latin1')

def addWordCounter(db, column):
    numberOfWords = []
    for line in range(len(db[column])):
        numberOfWords.append(len(str(db[column][line]).split()))
    db["Nb of Words"] = numberOfWords
    return db

countedDb = addWordCounter(data, "Article")

print(countedDb.head())