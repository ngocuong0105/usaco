#http://www.usaco.org/index.php?page=viewproblem2&cpid=944
# passes online IDE
from collections import defaultdict
from typing import Any
from utils import submit
from sys import setrecursionlimit
setrecursionlimit(10 ** 5)

def solve(inp) -> Any:
    def dfs(x,y):
        network.add((x,y))
        visited.add((x,y))
        for u,v in adj[x,y]:
            if (u,v) not in visited:
                dfs(u,v)
    def area(network):
        w = max(x for x,_ in network)-min(x for x,_ in network)
        h = max(y for _,y in network)-min(y for _,y in network)
        return 2*(w+h)

    cows, edges = inp
    res = float('inf')
    adj,visited = defaultdict(list),set()
    for u,v in edges:
        u, v = u-1, v-1
        adj[cows[u]].append(cows[v])
        adj[cows[v]].append(cows[u])
    for x,y in cows:
        if (x,y) not in visited:
            network = set()
            dfs(x,y)
            res = min(res,area(network))
    return res 

def read_input() -> tuple:
    N, M = tuple(map(int,input().split()))
    cows = [tuple(map(int,input().split())) for _ in range(N)]
    edges = [tuple(map(int,input().split())) for _ in range(M)]
    return cows, edges

submit(solve, read_input, test_cases=[6])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
