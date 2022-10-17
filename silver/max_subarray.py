n = int(input())
arr = list(map(int,input().split()))

res, curr = -float('inf'),0
for num in arr:
    curr += num
    res = max(res,curr)
    curr = max(curr,0)
print(res)