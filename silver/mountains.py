from typing import Any
from utils import submit

def get_intervals(peaks):
    intervals = []
    for x,y in peaks:
        intervals.append((x-y,x+y))
    return intervals

def solve(inp) -> Any:
    intervals = get_intervals(inp)
    intervals.sort(key = lambda x: (x[0],-x[1]))
    hidden,(s,e) = 0,intervals[0]
    for i,j in intervals[1:]:
        if s <= i  and j <= e:
            hidden += 1
        else:
            s,e = i,j
    return len(intervals) - hidden

def read_input() -> tuple:
    N = int(input())
    return [tuple(map(int,input().split())) for _ in range(N)]

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
