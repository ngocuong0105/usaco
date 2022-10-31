#http://www.usaco.org/index.php?page=viewproblem2&cpid=643
from itertools import accumulate
from typing import Any
from utils import submit

def solve(inp) -> Any:
    nums, K = inp
    nums.sort()
    l,j = [0]*len(nums),0
    for i in range(len(nums)):
        while j<len(nums) and nums[j]-nums[i] <= K:
            j += 1
        j -= 1
        l[i] = j-i+1
    r,i = [0]*len(nums),len(nums)-1
    for j in range(len(nums)-1,-1,-1):
        while i >= 0 and nums[j] - nums[i] <= K:
            i -= 1
        i += 1
        r[j] = j-i+1
    l = list(accumulate(l[::-1],max))[::-1]   
    r = list(accumulate(r,max))
    res = 0
    for i in range(len(l)-1):
        res = max(res,l[i+1]+r[i])
    return res

def read_input() -> tuple:
    N, K = tuple(map(int,input().split()))
    nums = [int(input()) for _ in range(N)]
    return nums, K 

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
