#https://cses.fi/problemset/task/1163/
from sortedcontainers import SortedList
from typing import Any
from utils import submit

def solve(inp) -> Any:
    x,nums = inp
    lights = SortedList([0,x])
    dist = SortedList([x])
    res = []
    for num in nums:
        i = lights.bisect_left(num)
        dist.add(lights[i]-num)
        if i: 
            dist.add(num-lights[i-1])
            dist.remove(lights[i]-lights[i-1])
        lights.add(num)
        res.append(str(dist[-1]))
    return ' '.join(res)

def read_input() -> tuple:
    x,n = tuple(map(int,input().split()))
    nums = list(map(int,input().split()))
    return x, nums

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
