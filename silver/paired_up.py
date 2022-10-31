#http://www.usaco.org/index.php?page=viewproblem2&cpid=738
from typing import Any
from utils import submit

def solve(inp) -> Any:
    count = inp
    count.sort(key = lambda x: x[1])
    i,j,res = 0,len(count)-1,0
    while i < j:
        cows = min(count[i][0],count[j][0])
        count[i][0] -= cows
        count[j][0] -= cows
        res = max(count[i][1]+count[j][1],res)
        i += count[i][0]==0
        j -= count[j][0]==0
    return res

def read_input() -> tuple:
    N = int(input())
    count = [list(map(int,input().split())) for _ in range(N)]
    return count

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
