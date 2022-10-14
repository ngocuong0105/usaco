from itertools import accumulate
from typing import Any
from utils import submit

def pref(arr,g):
    arr = [a==g for a in arr]
    return [0] + list(accumulate(arr))
def solve(arr) -> Any:
    mp = {}
    for g in 'SPH':
        mp[g] = pref(arr,g)
    res = 0
    
    for i in range(len(arr)+1):
        for g in 'SPH':
            for g1 in 'SPH':
                res = max(mp[g][i]+mp[g1][-1]-mp[g1][i],res)
    return res

def read_input() -> tuple:
    N = int(input())
    arr = [input() for _ in range(N)]
    return arr

submit(solve,read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
