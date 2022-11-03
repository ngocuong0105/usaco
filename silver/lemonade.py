#http://www.usaco.org/index.php?page=viewproblem2&cpid=835
from typing import Any
from utils import submit

def solve(inp) -> Any:
    N, nums = inp
    nums.sort(reverse = True)
    res,wait = 0,0
    for i in range(N):
        res += nums[i]>=wait
        wait += nums[i]>=wait    
    return res

def read_input() -> tuple:
    N = int(input())
    nums = list(map(int,input().split()))
    return N, nums

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
