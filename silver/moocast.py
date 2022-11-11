#http://www.usaco.org/index.php?page=viewproblem2&cpid=668
from collections import defaultdict
from typing import Any
from utils import submit


def solve(inp) -> Any:
    def dfs(x,y):
        visited.add((x,y))
        for u,v in adj[x,y]:
            if (u,v) not in visited:
                dfs(u,v)
    cows = inp
    adj = defaultdict(list)
    for i in range (len(cows)):
        x,y,p = cows[i]
        for j in range(len(cows)):
            a,b,_ = cows[j]
            if p**2 >= (x-a)**2 + (y-b)**2:
                adj[x,y].append((a,b))
    res = 0
    for x,y,_ in cows:
        visited = set()
        dfs(x,y)
        res = max(res,len(visited))
    return res

def read_input() -> tuple:
    N = int(input())
    cows = [tuple(map(int,input().split())) for _ in range(N)]
    return cows

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
