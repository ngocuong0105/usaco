#https://cses.fi/problemset/task/1629

n = int(input())
intervals = [list(map(int,input().split())) for _ in range(n)]
intervals.sort(key = lambda x: x[1])
res,curr = 0,-float('inf')
for s,e in intervals:
    if s >= curr:
        res += 1 
        curr = e
print(res)  
