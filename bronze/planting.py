from collections import defaultdict
import sys
sys.stdin = open("planting.in", "r")
sys.stdout = open("planting.out", "w")

N = int(input())
degree = defaultdict(int)
for _ in range(N-1):
    u,v = tuple(map(int,input().split()))
    degree[u] += 1
    degree[v] += 1
print(max(degree.values())+1)