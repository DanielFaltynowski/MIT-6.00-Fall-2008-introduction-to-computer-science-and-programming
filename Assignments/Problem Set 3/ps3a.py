def countSubStringMatch(target, key):
    counter = 0
    search = target.find(key)
    while search != -1:
        counter = counter + 1
        shift = search + len(key)
        target = target[shift:]
        search = target.find(key)
    return counter



def countSubStringMatchRecursive(target, key):
    search = target.find(key)
    if search == -1: return 0
    else: 
        shift = search + len(key)
        return 1 + countSubStringMatchRecursive(target[shift:], key)
    

print(countSubStringMatch("abcabcabcabc", "abc"))
print(countSubStringMatchRecursive("abcabcabcabc", "abc"))
print(countSubStringMatch("abcabcabcab", "abc"))
print(countSubStringMatchRecursive("abcabcabcab", "abc"))