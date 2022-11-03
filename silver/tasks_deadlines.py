#https://cses.fi/problemset/task/1630

n = int(input())
tasks = [tuple(map(int,input().split())) for _ in range(n)]
tasks.sort(key = lambda x: x[0])
curr,res = 0,0
for t,d in tasks:
    curr += t
    res += d-curr
print(res)