from collections import defaultdict
import sys
# sys.stdin = open("factory.in", "r")
# sys.stdout = open("factory.out", "w")
def dfs(s):
    if not adj[s]: return [s]
    res = []
    for u in adj[s]:
        res.extend(dfs(u))
    return res
N = int(input())
adj = defaultdict(list)
for _ in range(N-1):
    u,v = tuple(map(int,input().split()))
    adj[u].append(v)
res = None
for s in range(1,N+1):
    final = dfs(s)
    if len(final)>1 or res not in [final[0],None]:
        print(-1)
        break
    res = final[0]
else:
    print(res)