from collections import Counter
from itertools import accumulate


n, x= tuple(map(int,input().split()))
nums = list(map(int,input().split()))
cum = [0] + list(accumulate(nums))
d,res = Counter(),0
d[0] = 1
for num in cum[1:]:
    res += d[num-x]
    d[num] += 1
print(res)