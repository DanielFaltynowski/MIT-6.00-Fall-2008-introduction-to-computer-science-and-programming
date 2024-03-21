def bubbleSort(L):
    swapped = True
    n = len(L) - 1
    while swapped and n > 0:
        swapped = False
        i = 0
        while i < n:
            if L[i] > L[i + 1]:
                temp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = temp
                swapped = True
            i = i + 1
        n = n - 1
    return L


print(bubbleSort([1, 2, 3, 4]))
print(bubbleSort([4, 3, 2, 1]))
print(bubbleSort([1, 7, 2, 9, 3, 5, 3, 9]))
print(bubbleSort([9, 1, 7, 2, 9, 3, 5, 3]))
print(bubbleSort([9, 7, 2, 9, 3, 5, 3, 1]))