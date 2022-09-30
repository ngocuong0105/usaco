import sys
sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

from collections import defaultdict
N, M = tuple(map(int,input().split()))

spot = [input() for _ in range(N)]
plain = [input() for _ in range(N)]

s,p = defaultdict(set),defaultdict(set)
for i in range(N):
    for a in range(M-2):
        for b in range(a+1,M-1):
            for c in range(b+1,M):
                s[a,b,c].add(spot[i][a]+spot[i][b]+spot[i][c])
                p[a,b,c].add(plain[i][a]+plain[i][b]+plain[i][c])
res = set()
for a in range(M-2):
    for b in range(a+1,M-1):
        for c in range(b+1,M):
            if len(s[a,b,c] & p[a,b,c]) == 0:
                res.add((a,b,c)) 
print(len(res))