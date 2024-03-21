def selectionSort(L):
    pointer = 0
    while pointer < len(L):
        i = pointer
        min = pointer
        while i < len(L):
            if L[i] < L[min]:
                min = i
            i = i + 1
        temp = L[pointer]
        L[pointer] = L[min]
        L[min] = temp
        pointer = pointer + 1
    return L


print(selectionSort([1, 2, 3, 4]))
print(selectionSort([4, 3, 2, 1]))
print(selectionSort([1, 7, 2, 9, 3, 5, 3, 9]))
print(selectionSort([9, 1, 7, 2, 9, 3, 5, 3]))
print(selectionSort([9, 7, 2, 9, 3, 5, 3, 1]))