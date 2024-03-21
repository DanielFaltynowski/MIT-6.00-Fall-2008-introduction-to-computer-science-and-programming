def merge(LL, LR):
    ans = []
    i = 0
    j = 0
    while i < len(LL) and j < len(LR):
        if LL[i] <= LR[j]:
            ans.append(LL[i])
            i = i + 1
        else:
            ans.append(LR[j])
            j = j + 1
    while i < len(LL):
        ans.append(LL[i])
        i = i + 1
    while j < len(LR):
        ans.append(LR[j])
        j = j + 1
    return ans


def mergeSort(L):
    if len(L) < 2:
        return L
    else:
        mid = len(L) // 2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        ans = merge(left, right)
        return ans


print(mergeSort([1, 2, 3, 4]))
print(mergeSort([4, 3, 2, 1]))
print(mergeSort([1, 7, 2, 9, 3, 5, 3, 9]))
print(mergeSort([9, 1, 7, 2, 9, 3, 5, 3]))
print(mergeSort([9, 7, 2, 9, 3, 5, 3, 1]))