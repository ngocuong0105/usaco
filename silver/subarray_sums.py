#https://cses.fi/problemset/task/1660
from collections import Counter
from itertools import accumulate


n, t = tuple(map(int,input().split()))
nums = [0]+list(accumulate(list(map(int,input().split()))))
c,res = Counter(),0
for num in nums:
    res += c[num-t]
    c[num] += 1
print(res)
