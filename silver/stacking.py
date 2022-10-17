from itertools import accumulate
from typing import Any
from utils import submit

def solve(inp) -> Any:
    N, intervals = inp
    cum = [0]*(N+1)
    for a,b in intervals:
        cum[a-1] += 1
        cum[b] -= 1
    return sorted(list(accumulate(cum)))[(N+1)//2]

def read_input() -> tuple:
    N, K = tuple(map(int,input().split()))
    intervals = [tuple(map(int,input().split())) for _ in range(K)]
    return N, intervals

submit(solve,read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
