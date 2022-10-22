from typing import Any
from utils import submit

def solve(inp) -> Any:
    times = inp
    events = [(s,True,i) for i,(s,_) in enumerate(times)] + [(e,False,i) for i,(_,e) in enumerate(times)]
    events.sort()
    prev,total,active = 0,0,set()
    alone_time = [0]*len(times)
    for t,is_start,i in events:
        if active:
            total += t-prev
        if len(active) == 1:
            alone_time[next(iter(active))] = t-prev
        if is_start:
            active.add(i)
        else:
            active.remove(i)
        prev = t
    return total - min(alone_time)

def read_input() -> tuple:
    N = int(input())
    times = [tuple(map(int,input().split())) for _ in range(N)]
    return times

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
