from typing import Any
from utils import submit

# O(N^3)
def solve_brute(inp) -> Any:
    coords,res = inp,0
    xs = {num:i for i,num in enumerate(sorted([x for x,_ in coords]))}
    ys = {num:i for i,num in enumerate(sorted([y for _,y in coords]))}
    coords = [(xs[x],ys[y]) for x,y in coords]
    for i in range(len(coords)):
        for j in range(i+1,len(coords)):
            a,b = coords[i],coords[j]
            l,r = 0,0
            for x,y in coords:
                if (min(a[1],b[1]) <= y <= max(a[1],b[1])):
                    l += x <= min(a[0],b[0]) 
                    r += x >= max(a[0],b[0])
            res += l*r                
    return res + len(coords) + 1

# O(N^2)
def get(cum, x1, y1, x2, y2):
    return cum[x2][y2] - cum[x2][y1-1] - cum[x1-1][y2] + cum[x1-1][y1-1]
 
def solve(inp):
    N, P = inp
    xs = {num:i+1 for i,num in enumerate(sorted([x for x,_ in P]))}
    ys = {num:i+1 for i,num in enumerate(sorted([y for _,y in P]))}
    P = [(xs[x],ys[y]) for x,y in P]

    cum = [[0]*(N+1) for _ in range(N+1)]
    for x,y in P:
        cum[x][y] = 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            cum[i][j] += cum[i-1][j] + cum[i][j-1] - cum[i-1][j-1]
    res = 0
    for i in range(N):
        for j in range(i,N):
            x1 = min(P[i][0], P[j][0])
            x2 = max(P[i][0], P[j][0])
            y1 = min(P[i][1], P[j][1])
            y2 = max(P[i][1], P[j][1]) 
            res += get(cum,1,y1,x1,y2) * get(cum,x2,y1,N,y2)
    return res + 1

def read_input() -> tuple:
    N = int(input())
    coords = [tuple(map(int,input().split())) for  _ in range(N)]
    return N,coords

submit(solve, read_input, test_cases=[1,2,3])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
