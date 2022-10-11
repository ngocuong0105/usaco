from itertools import product
from typing import Any
from utils import submit


def f1(sign,c):
    return sorted(c, key = lambda x: sign * x[0])[:4]

def f2(sign,c):
    return sorted(c,key = lambda x: sign * x[1])[:4]

def get_rect(a,b,c,d):
    return (min(a[0],b[0],c[0],d[0]),max(a[0],b[0],c[0],d[0]),min(a[1],b[1],c[1],d[1]),max(a[1],b[1],c[1],d[1]))

def points(a,b,c,d,cows):
    rect = get_rect(a,b,c,d)
    return sum(inside(rect,u,v) for u,v in cows)

def inside(rect,x,y):
    return rect[0] <= x <= rect[1] and rect[2] <= y <= rect[3]
  
def area(a,b,c,d):
    l,r,u,d = get_rect(a,b,c,d)
    return abs((r-l)*(u-d))

def solve(inp) -> Any:
    N, cows = inp
    l,r = f1(1,cows), f1(-1,cows)
    u,d = f2(1,cows), f2(-1,cows)
    res =  float('inf')
    for a,b,c,d in product(l,r,u,d):
        if points(a,b,c,d,cows) >= N - 3:
            res = min(res,area(a,b,c,d))
    return res

def read_input() -> tuple:
    N = int(input())
    cows = []
    for _ in range(N):
        cows.append(tuple(map(int,input().split())))
    return N, cows

submit(solve,read_input,test_cases = [])
#%%
from utils import print_mismatch
print_mismatch(test_cases = [])
# %%
