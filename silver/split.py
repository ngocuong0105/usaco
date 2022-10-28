# http://www.usaco.org/index.php?page=viewproblem2&cpid=645
from heapq import heappush
from typing import Any
from utils import submit

def min_enclosure(cows):
    minn,maxx = [cows[0][1]],[-cows[0][1]]
    l = cows[0][0]
    left = [0]
    for x,y in cows[1:]:
        heappush(minn,y)
        heappush(maxx,-y)
        w = x-l
        h = -maxx[0]-minn[0]
        left.append(w*h)
    minn,maxx = [cows[-1][1]],[-cows[-1][1]]
    r = cows[-1][0]
    right = [0]
    for x,y in cows[::-1][1:]:
        heappush(minn,y)
        heappush(maxx,-y)
        w = r-x
        h = -maxx[0]-minn[0]
        right.append(w*h)
    right.reverse()
    return min(a+b for a,b in zip(left,right[1:]))

def solve(inp) -> Any:
    cows = inp
    l,r = min(i for i,_ in cows),max(i for i,_ in cows)
    d,u = min(j for _,j in cows),max(j for _,j in cows)
    area1 = (r-l)*(u-d)
    cows.sort(key = lambda x: (x[0],-x[1]))
    area2 = min(min_enclosure(cows),min_enclosure(sorted([(y,x) for x,y in cows],key = lambda x:(x[0],-x[1]))))
    return area1 - area2

def read_input() -> tuple:
    N = int(input())
    return [tuple(map(int,input().split())) for _ in range(N)]

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
