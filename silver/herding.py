#http://www.usaco.org/index.php?page=viewproblem2&cpid=918
from typing import Any
from utils import submit

def solve_min(nums):
    if nums[-2]-nums[0]+1 == len(nums)-1 and nums[-1]-nums[-2]>2: return 2
    if nums[-1]-nums[1]+1 == len(nums)-1 and nums[1]-nums[0]>2: return 2
    res,j = 0,0
    for i in range(len(nums)):
        while j<len(nums) and nums[j]-nums[i]<len(nums):
            j += 1
        res = max(res,j-i)
    return len(nums) - res
    
def solve_max(nums):
    return nums[-1]-nums[0]+1-len(nums)-min(nums[1]-nums[0],nums[-1]-nums[-2])+1
def solve(inp) -> Any:
    nums = inp
    nums.sort()
    return solve_min(nums),solve_max(nums)

def read_input() -> tuple:
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    return nums

submit(solve, read_input, test_cases=[], new_line=True)

#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
