import sys
# sys.stdin = open("lifeguards.in", "r")
# sys.stdout = open("lifeguards.out", "w")

N = int(input())
intervals = []
for _ in range(N):
    intervals.append(tuple(map(int,input().split())))

covered = [0]*1001
for s,e in intervals:
    for p in range(s,e):
        covered[p] += 1
res = 0
for s,e in intervals:
    c = list(covered)
    for p in range(s,e):
        c[p] -= 1
    res = max(res,len(c)-c.count(0))
    print(c[:10])
print(res)
        