N = int(input())
stmt,points = [],[]
for _ in range(N):
    a,b = input().split() 
    stmt.append([a,int(b)])
    points.append(int(b))
res = float('inf')
for p in points:
    cnt = 0
    for a,b in stmt:
        if a == 'G' and b > p: cnt += 1
        elif a == 'L' and b < p: cnt += 1
    res = min(res,cnt)
print(res)