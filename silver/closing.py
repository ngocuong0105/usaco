#http://www.usaco.org/index.php?page=viewproblem2&cpid=644
#http://www.usaco.org/index.php?page=viewproblem2&cpid=646
from collections import defaultdict
from typing import Any
from utils import submit

class DSU:

    def __init__(self):
        self.rank = {}
        self.parent = {}
        self.components = 0

    def add(self,x):
        self.rank[x] = 0
        self.parent[x] = x
        self.components += 1

    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        u,v = self.find(x),self.find(y)
        if u == v: return
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1
        self.components -= 1
    
def solve(inp) -> Any:
    N, queries, edges = inp
    queries.reverse()
    adj,dsu,res = defaultdict(list),DSU(),[]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for s in queries:
        dsu.add(s)
        for u in adj[s]:
            if u in dsu.rank:
                dsu.union(s,u)
        res.append('YES' if dsu.components == 1 else 'NO')
    return res[::-1]

def read_input() -> tuple:
    N, M = tuple(map(int,input().split()))
    edges = [tuple(map(int,input().split())) for _ in range(M)]
    queries = [int(input()) for _ in range(N)]
    return N, queries, edges

submit(solve, read_input, test_cases=[], new_line=True)
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
