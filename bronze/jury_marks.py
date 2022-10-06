from collections import Counter
from itertools import accumulate

k,n = tuple(map(int,input().split()))
nums = list(map(int,input().split()))
need = list(map(int,input().split()))

cum = list(accumulate(nums))
v = need[0]
res = set()
for num in cum:
    s = need[0]-num
    c = Counter(cum)
    for v in need:
        if c[v-s] == 0:
            break
        c[v-s] -= 1
    else:
        res.add(s)
print(len(res))
