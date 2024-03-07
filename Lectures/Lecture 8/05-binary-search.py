def binary_search(s, e):
    left = 0
    right = len(s) - 1
    while left <= right:
        mid = (left + right) // 2
        if e == s[mid]:
            return True
        elif e < s[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False


print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 8))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 0))