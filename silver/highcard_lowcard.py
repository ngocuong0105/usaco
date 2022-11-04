#http://www.usaco.org/index.php?page=viewproblem2&cpid=573
from typing import Any
from utils import submit

def solve(inp) -> Any:
    N, elsie = inp
    s = set(elsie)
    bessie = [num for num in range(1,2*N+1) if num not in s]
    elsie = sorted(elsie[:N//2]) + sorted([-num for num in elsie[N//2:]])
    bessie = sorted(bessie,reverse = True)
    bessie = sorted(bessie[:N//2]) + sorted([-num for num in bessie[N//2:]])
    def highest_card(e,b):
        j,res = 0,0
        for i in range(N//2):
            while j < N//2 and e[i] > b[j]:
                j += 1
            if j < N//2:
                j += 1
                res += 1
        return res
    return highest_card(elsie[:N//2],bessie[:N//2]) + highest_card(elsie[N//2:],bessie[N//2:])

def read_input() -> tuple:
    N = int(input())
    elsie = [int(input()) for _ in range(N)]
    return N,elsie

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
