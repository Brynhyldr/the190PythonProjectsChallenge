from collections import defaultdict

listToOrder = ["tea", "eat", "bat", "ate", "arc", "car"]

def group_anagram(listToOrder):
    d = defaultdict(list)
    for i in listToOrder:
        sort_item = " ".join(sorted(i))
        d[sort_item].append(i)
    return d