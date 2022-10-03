from itertools import permutations
import sys
sys.stdin = open("lineup.in", "r")
sys.stdout = open("lineup.out", "w")

N = int(input())

edges = []
for _ in range(N):
    s = input().split()
    edges.append([s[0],s[-1]])

cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue']
res = ('Z')
for order in permutations(cows,8):
    for u,v in edges:
        if abs(order.index(u)-order.index(v)) != 1:
            break
    else:
        res = min(res,order)
for c in res: print(c)
