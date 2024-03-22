def subStringMatchExact(target, key):
    ans = []
    i = 0
    search = target.find(key)
    while search != -1 and len(key) != 0:
        i = i + search
        ans.append(i)
        i = i + len(key)
        shift = search + len(key)
        target = target[shift:]
        search = target.find(key)
    return tuple(ans)


def constrainedMatchPair(match1, match2, keyLength):
    if len(match2) == 0:
        return list(match1)
    else:
        ans = []
        i = 0
        j = 0
        while i < len(match1) and j < len(match2):
            if match1[i] + keyLength + 1 == match2[j]:
                ans.append(match1[i])
                j = j + 1
            i = i + 1
        return ans


def myTest():
    sub1 = subStringMatchExact("abcdadcdabcd", "a")
    sub2 = subStringMatchExact("abcdadbdabcd", "cd")
    print(sub1)
    print(sub2)
    contained = constrainedMatchPair(sub1, sub2, len("a"))
    print(contained)


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = []
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print('breaking key',key,'into',key1,key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        print("hey")
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print('match1',match1)
        print('match2',match2)
        print('possible matches for',key1,key2,'start at',filtered)
    return allAnswers


myTest()
subStringMatchOneSub("abcd", "abcdeabcdeabcde")
subStringMatchOneSub("abcd", "abcdeadcdeabcde")


