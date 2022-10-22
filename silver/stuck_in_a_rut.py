# http://www.usaco.org/index.php?page=viewproblem2&cpid=1064
from typing import Any
from utils import submit

def cross(x,y,a,b):
    return x > a and b > y

def solve(inp) -> Any:
    cows = inp
    north = [(i,x,y) for i,dr,x,y  in cows if dr == 'N']
    east = [(i,x,y) for i,dr,x,y in cows if dr == 'E']
    north.sort(key = lambda x: x[1])
    east.sort(key = lambda x: x[2])
    res = [0]*len(cows)
    stopped = [False]*len(cows)
    for i,x,y in north:
        for j,a,b in east:
            if not cross(x,y,a,b) or i == j: continue
            if not stopped[i] and not stopped[j]:
                if b-y < x-a:
                    res[i] += res[j] + 1
                    stopped[j] = True
                elif b-y > x-a:
                    res[j] += res[i] + 1
                    stopped[i] = True
    return res

def read_input() -> tuple:
    N = int(input())
    cows = []
    for i in range(N):
        dr,x,y = input().split()
        cows.append((i,dr,int(x),int(y)))
    return cows

submit(solve, read_input, test_cases=[], new_line=True)
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])