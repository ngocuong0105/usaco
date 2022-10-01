import sys
sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

from collections import defaultdict

N = int(input())
cows = []
for _ in range(N):
    x,y = tuple(map(int,input().split()))
    cows.append((x,y))
res = float('inf')
cows.sort()
for _,yf in cows:
    yf += 1
    quad = defaultdict(int)
    for _,y in cows:
        quad[True, yf > y] += 1
    for x,y in cows:
        xf = x+1
        quad[False,yf > y] += 1
        quad[True,yf > y] -= 1
        res = min(res,max(quad.values()))
print(res)
# fix y fence and line sweep on x