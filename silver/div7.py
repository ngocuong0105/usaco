from itertools import accumulate
from typing import Any
from utils import submit

def solve(nums) -> Any:
    nums = [num%7 for num in nums]
    cum = [0]+list(accumulate(nums))
    cum = [num%7 for num in cum]
    f,l = {},{}
    for i in range(len(cum)):
        if cum[i] not in f:
            f[cum[i]] = i
        l[cum[i]] = i 
    return max(l[r]-f[r] for r in f)
 
def read_input() -> tuple:
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    return nums

submit(solve,read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
