#http://www.usaco.org/index.php?page=viewproblem2&cpid=594
from typing import Any
from utils import submit

def shooted_all(N, K, radius, nums):
    i = 0
    while i < N and K:
        j = i+1
        while j < N and nums[j]-nums[i] <= 2*radius:
            j += 1
        i = j
        K -= 1
    return i == N

def solve(inp) -> Any:
    N, K, nums = inp
    nums.sort()
    l,r = 0,nums[-1]
    while l < r:
        radius = l+r >> 1
        if shooted_all(N, K,radius, nums):
            r = radius
        else:
            l = radius+1  
    return l

def read_input() -> tuple:
    N, K = tuple(map(int,input().split()))
    nums = [int(input()) for _ in range(N)]
    return N, K, nums

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
