#https://codeforces.com/problemset/problem/701/C
from collections import Counter

n = int(input())
s = input()
res,i = float('inf'),-1
seen,t = Counter(),len(set(s))
for j in range(n):
    seen[s[j]] += 1
    while len(seen) == t:
        res = min(res,j-i)
        i += 1
        seen[s[i]] -= 1
        if seen[s[i]] == 0: del seen[s[i]]
print(res)