#https://cses.fi/problemset/task/1084
from sortedcontainers import SortedList

from typing import Any
from utils import submit

def solve(inp) -> Any:
    a,b,k = inp
    res = 0
    for x in b:
        i = a.bisect_left(x)
        if i and x-a[i-1] <= k: 
            a.remove(a[i-1])
            res += 1
        elif i < len(a) and a[i]-x <= k: 
            a.remove(a[i])
            res += 1
    return res

def read_input() -> tuple:
    n,m,k = tuple(map(int,input().split()))
    a = SortedList(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    return a,b,k

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
