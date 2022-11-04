#https://codeforces.com/problemset/problem/1158/A
from heapq import heappop, heappush

# O(mlog(n) + n)
# There is O(m+n) solution using maths, see https://codeforces.com/blog/entry/66993
def solve(inp):
    n,m,minn,maxx = inp
    res = sum(m*num for num in minn)
    h = [(-num,m-1) for num in minn]
    for num in maxx:
        sweets,cnt = heappop(h)
        if -sweets>num: return -1
        res += num+sweets
        cnt -= -sweets != num
        if cnt: heappush(h,(sweets,cnt))
    return res

n, m = tuple(map(int,input().split()))
minn = list(map(int,input().split()))
maxx = list(map(int,input().split())) 
print(solve((n,m,minn,maxx)))

