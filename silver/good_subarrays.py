from collections import Counter
from itertools import accumulate


def solve(nums,n):
    cum = [0]+list(accumulate(nums))
    c = Counter([v-i for i,v in enumerate(cum)])
    return sum((v*(v-1))//2 for v in c.values())

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int,list(input())))
    print(solve(nums,n))