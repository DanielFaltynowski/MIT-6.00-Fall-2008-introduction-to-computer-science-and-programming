def subStringMatchExact(target, key):
    ans = []
    i = 0
    search = target.find(key)
    while search != -1:
        i = i + search
        ans.append(i)
        i = i + len(key)
        shift = search + len(key)
        target = target[shift:]
        search = target.find(key)
    return tuple(ans)


# print(subStringMatchExact("abcabcabcabc", "abc"))
# print(subStringMatchExact("abcabcabcab", "abc"))

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

print(subStringMatchExact(target1, key10))
print(subStringMatchExact(target1, key11))
print(subStringMatchExact(target1, key12))
print(subStringMatchExact(target1, key13))
print(subStringMatchExact(target2, key10))
print(subStringMatchExact(target2, key11))
print(subStringMatchExact(target2, key12))
print(subStringMatchExact(target2, key13))