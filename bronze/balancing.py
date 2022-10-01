import sys
sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

from collections import defaultdict

N,B = tuple(map(int,input().split()))
xs,ys = [],[]
for _ in range(N):
    x,y = tuple(map(int,input().split()))
    xs.append(x)
    ys.append(y)
res = float('inf')
for xf in xs:
    for yf in ys:
        for dx,dy in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            xf,yf = xf+dx,yf+dy
            quad = defaultdict(int)
            for x,y in zip(xs,ys):
                quad[x>xf,y>yf] += 1
            res = min(res,max(quad.values()))
print(res)