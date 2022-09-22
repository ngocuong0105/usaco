import sys
sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

from itertools import accumulate
N = int(input())
intervals = []
for _ in range(N):
    intervals.append(tuple(map(int,input().split()))) 
times = [0]*1002
for s,e,cnt in intervals:
    times[s] = cnt
    times[e] = -cnt
print(max(accumulate(times)))