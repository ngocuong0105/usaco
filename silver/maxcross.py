from itertools import accumulate
from typing import Any
from utils import submit

def solve(inp) -> Any:
    K,arr = inp
    cum = [0] + list(accumulate(arr))
    res = float('inf')
    for i in range(len(cum)-K):
        res = min(cum[i+K]-cum[i],res)
    return res

def read_input() -> tuple:
    N, K, B = tuple(map(int,input().split())) 
    arr = [0]*N
    for _ in range(B):
        arr[int(input())-1] = 1
    return K,arr

submit(solve,read_input, test_cases=[])
# #%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
