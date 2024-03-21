def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element: ')
        if elem == '':
            done = True
        else:
            res.append(elem)
    temp = res
    temp.reverse()
    isPalindrome = res == temp
    if isPalindrome: print('IS palindrome') 
    else: print('IS NOT palindrome') 


def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element: ')
        if elem == '':
            done = True
        else:
            res.append(elem)
    print('res should be [1, a, 2]', res) # ERROR IS NOT THERE
    temp = res
    temp.reverse()
    isPalindrome = res == temp
    if isPalindrome: print('IS palindrome') 
    else: print('IS NOT palindrome') 


def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element: ')
        if elem == '':
            done = True
        else:
            res.append(elem)
    # print('res should be [1, a, 2]', res) # ERROR IS NOT THERE
    temp = res
    temp.reverse()
    isPalindrome = res == temp
    print('temp', temp, 'res', res) # REMEMBER that `temp` is a POINTER to `res`
    if isPalindrome: print('IS palindrome') 
    else: print('IS NOT palindrome') 


def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element: ')
        if elem == '':
            done = True
        else:
            res.append(elem)
    # print('res should be [1, a, 2]', res) # ERROR IS NOT THERE
    temp = res
    print('temp', temp, 'res', res) # THERE `temp` & `res` are reversed
    temp.reverse()
    isPalindrome = res == temp
    # print('temp', temp, 'res', res) # REMEMBER that `temp` is a POINTER to `res`
    if isPalindrome: print('IS palindrome') 
    else: print('IS NOT palindrome') 


def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element: ')
        if elem == '':
            done = True
        else:
            res.append(elem)
    # print('res should be [1, a, 2]', res) # ERROR IS NOT THERE
    temp = res
    # print('temp', temp, 'res', res) # THERE `temp` & `res` are reversed
    temp.reverse()
    print('temp', temp, 'res', res) # THERE IS A PROBLEM
    isPalindrome = res == temp
    # print('temp', temp, 'res', res) # REMEMBER that `temp` is a POINTER to `res`
    if isPalindrome: print('IS palindrome') 
    else: print('IS NOT palindrome') 


def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element: ')
        if elem == '':
            done = True
        else:
            res.append(elem)
    # print('res should be [1, a, 2]', res) # ERROR IS NOT THERE
    temp = res[:] # FIXED!!!
    # print('temp', temp, 'res', res) # THERE `temp` & `res` are reversed
    temp.reverse()
    # print('temp', temp, 'res', res) # THERE IS A PROBLEM
    isPalindrome = res == temp
    # print('temp', temp, 'res', res) # REMEMBER that `temp` is a POINTER to `res`
    if isPalindrome: print('IS palindrome') 
    else: print('IS NOT palindrome') 


silly()