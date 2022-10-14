from typing import Any
from utils import submit

def _solve(t):
    N, hunger = t
    sm = sum(hunger)
    for i in range(N-1):
        if hunger[i] < hunger[i+1]:
            diff = hunger[i+1] - hunger[i]
            hunger[i+1] -= diff
            if i+2 >= N: return -1
            hunger[i+2] -= diff
            if hunger[i+2] < 0: return -1
        elif hunger[i] > hunger[i+1]:
            if i % 2 == 0: return -1
    return sm - min(hunger) * N

def solve(inp) -> Any:
    tests = inp
    res = []
    for t in tests:
        res.append(_solve(t))
    return res

def read_input() -> tuple:
    T = int(input())
    tests = []
    for _ in range(T):
        N = int(input())
        hunger = list(map(int,input().split()))
        tests.append((N,hunger))
    return tests

submit(solve,read_input, test_cases=[], new_line = True)

# # #%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
