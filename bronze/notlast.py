import sys

sys.stdin = open("notlast.in", "r")
sys.stdout = open("notlast.out", "w")

N = int(input())
d = {'Bessie':0, 'Elsie':0, 'Daisy':0, 'Gertie':0, 'Annabelle':0, 'Maggie':0, 'Henrietta':0}
for _ in range(N):
    cow, milk = input().split()
    d[cow] += int(milk)
M = min(d.values())
res = float('inf')
for key,v in d.items():
    if v > M: 
        if v < res:
            res = v
            k = key
if sum([res == v for v in d.values()]) != 1: print('Tie')
else: print(k)