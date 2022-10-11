from collections import defaultdict
import sys
sys.stdin = open("revegetate.in", "r")
sys.stdout = open("revegetate.out", "w")

N, M = tuple(map(int,input().split()))
adj = defaultdict(list)
for _ in range(M):
    u,v = tuple(map(int,input().split()))
    adj[(min(u,v))].append(max(u,v))

res = [set([1,2,3,4]) for _ in range(N+1)]
for s in range(1,N+1):
    res[s] = min(res[s])
    for u in adj[s]:
        res[u] -= {res[s]}
print(''.join([str(i) for i in res[1:]]))