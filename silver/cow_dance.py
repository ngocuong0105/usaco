#http://www.usaco.org/index.php?page=viewproblem2&cpid=690
from heapq import heappop, heappush
from typing import Any
from utils import submit

def time(k,nums):
    t,h = 0,[]
    for num in nums:
        heappush(h,t+num)
        if len(h) == k:
            t = heappop(h)
    return max(h+[t])

def solve(inp) -> Any:
    N, T, nums = inp
    l, r = 0, N
    while l < r:
        m = l+r >> 1
        if time(m,nums) <= T:
            r = m
        else:
            l = m+1 
    return l

def read_input() -> tuple:
    N, T = tuple(map(int,input().split()))
    nums = [int(input()) for _ in range(N)] 
    return N, T, nums

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
