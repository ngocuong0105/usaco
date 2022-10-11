from collections import Counter


def solve(a,b,c):
    mp = Counter()
    for j in range(len(c)):
        mp[b[c[j]]] += 1
    res = 0
    for num in a:
        res += mp[num]
    return res