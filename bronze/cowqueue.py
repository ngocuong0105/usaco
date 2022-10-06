from collections import deque
import sys
sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

N = int(input())
cows = []
for _ in range(N):
    cows.append(tuple(map(int,input().split())))
cows.sort(key = lambda x: (x[0],x[0]+x[1]))
q = deque(cows)
curr = 0
while q:
    s,t = q.popleft()
    curr = max(curr,s) + t
print(curr)