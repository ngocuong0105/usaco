#http://www.usaco.org/index.php?page=viewproblem2&cpid=858
from typing import Any
from utils import submit

def count(nums,wait,cap):
    buses,curr,first = 1,1,nums[0]
    for t in nums[1:]:
        if curr + 1 <= cap and t-first <= wait:
            curr += 1
        else:
            first = t
            curr = 1
            buses += 1
    return buses

def solve(inp) -> Any:
    N, M, C, nums = inp
    nums.sort()
    l,r = 0,nums[-1]
    while l < r:
        max_wait = l+r >> 1
        if count(nums,max_wait,C) <= M:
            r = max_wait
        else:
            l = max_wait+1
    return l

def read_input() -> tuple:
    N, M, C = tuple(map(int,input().split()))
    nums = list(map(int,input().split()))
    return N, M, C, nums

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
