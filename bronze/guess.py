import sys
sys.stdin = open("guess.in", "r")
sys.stdout = open("guess.out", "w")

from collections import defaultdict

N = int(input())
animals = defaultdict(set)
for _ in range(N):
    t = input().split()
    animals[t[0]] = set(t[2:])
res = 1
for s1 in animals.values():
    for s2 in animals.values():
        if s1 == s2: continue
        res = max(res,1+len(s1 & s2))
print(res)