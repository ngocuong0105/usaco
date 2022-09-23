import sys
sys.stdin = open("mowing.in", "r")
sys.stdout = open("mowing.out", "w")


N = int(input())
dr = {'E':(0,1),'W':(0,-1),'N':(1,0),'S':(-1,0)}
visited = {}
res,time = float('inf'),0
i,j = 0,0
visited[i,j] = time
for _ in range(N):
    d, s = tuple(input().split())
    for _ in range(int(s)):
        i += dr[d][0]
        j += dr[d][1]
        time += 1
        if (i,j) in visited:
            res = min(res,time-visited[i,j])
        visited[i,j] = time
print(res) if res != float('inf') else print(-1)