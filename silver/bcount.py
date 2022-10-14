from itertools import accumulate
from typing import Any
from utils import submit

def query(l,r,cum):
    return cum[r] - cum[l-1]

def pref(nums,i):
    nums = [num==i for num in nums]
    return [0] + list(accumulate(nums))

def solve(inp) -> Any:
    nums,q = inp
    res,mp = [],{}
    for i in range(1,4):
        mp[i] = pref(nums,i)
    for l,r in q:
        vals = [0,0,0]
        for i in range(1,4):
            vals[i-1] = str(query(l,r,mp[i]))
        res.append(' '.join(vals))
    return res

def read_input() -> tuple:
    N, Q = tuple(map(int,input().split()))
    nums,q = [],[]
    for _ in range(N):
        nums.append(int(input()))
    for _ in range(Q):
        q.append(tuple(map(int,input().split())))
    return nums,q

submit(solve,read_input, test_cases=[], new_line=True)

# %%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
