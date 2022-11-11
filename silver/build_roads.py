#https://cses.fi/problemset/task/1666
from collections import defaultdict
import sys
sys.setrecursionlimit(1500000)

def dfs(s):
    visited.add(s)
    for u in adj[s]:
        if u not in visited:
            dfs(u)

n, m = tuple(map(int,input().split()))
edges = [tuple(map(int,input().split())) for _ in range(m)]
adj = defaultdict(list)
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)

res,visited,prev = [],set(),None
for s in range(1,n+1):
    if s not in visited:
        if prev: res.append((prev,s))
        dfs(s)
        prev = s

print(len(res))
for a,b in res:
    print(a,b)

