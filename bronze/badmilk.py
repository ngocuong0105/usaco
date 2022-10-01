import sys
sys.stdin = open("badmilk.in", "r")
sys.stdout = open("badmilk.out", "w")

from collections import defaultdict
N, M, D, S = tuple(map(int,input().split()))
drinks,sick = defaultdict(list), defaultdict(list)
for _ in range(D):
    p,m,t = tuple(map(int,input().split()))
    drinks[p].append((m,t))
for _ in range(S):
    p,t = tuple(map(int,input().split()))
    sick[p].append(t)

bad_milk = set(i for i in range(1,M+1))
for p in sick:
    for sick_time in sick[p]:
        for m in range(1,M+1):
            if m in bad_milk and m not in [mm for mm, drink_time in drinks[p] if sick_time > drink_time]:
                bad_milk.remove(m)
res = 0
for m in bad_milk:
    curr = set()
    for p in drinks:
        if m in [mm for mm,_ in drinks[p]]:
            curr.add(p)
    res = max(res, len(curr))
print(res)