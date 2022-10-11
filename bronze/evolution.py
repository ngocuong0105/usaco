from collections import defaultdict
import sys
sys.stdin = open("evolution.in", "r")
sys.stdout = open("evolution.out", "w")

N = int(input())
sets = defaultdict(set)
for i in range(N):
    features = input().split()[1:]
    for f in features:
        sets[f].add(i)
res = 'yes'
for u in sets:
    for v in sets:
        a,b,c = len(sets[u]-sets[v]), len(sets[v]-sets[u]), len(sets[u] & sets[v])
        if a and b and c:
            res = 'no'
            break
    if res == 'no': break
print(res)
