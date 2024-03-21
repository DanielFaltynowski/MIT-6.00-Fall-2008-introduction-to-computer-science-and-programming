def createHashTable(smallest, largest):
    intSet = []
    for i in range(smallest, largest + 1):
        intSet.append(None)
    return intSet


def insert(intSet, e):
    intSet[e] = 1


def member(intSet, e):
    if intSet[e] == 1:
        return True
    else:
        return False