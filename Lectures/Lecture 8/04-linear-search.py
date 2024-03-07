def linear_search(s, e):
    ans = None
    i = 0
    numCompares = 0
    while i < len(s) and ans == None:
        numCompares = numCompares + 1
        if e == s[i]: ans = True
        elif e < s[i]: ans = False
        i = i + 1
    return ans, numCompares


print(linear_search([1, 2, 3, 4], 3))
print(linear_search([1, 2, 3, 4], 5))
print(linear_search([1, 2, 3, 4], 0))