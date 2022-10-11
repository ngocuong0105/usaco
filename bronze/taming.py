import sys
sys.stdin = open("taming.in", "r")
sys.stdout = open("taming.out", "w")

N = int(input())
logs = list(map(int,input().split()))
breaks = [-1]*N # -1 unknown, 0 is no breakout, 1 breakout
breaks[0] = 1
done = False

for i in range(N):
    if logs[i] > -1:
        breaks[i-logs[i]] = 1
        for ii in range(i-logs[i]+1,i+1):
            breaks[ii] = 0
        for ii in range(1,logs[i]+1):
            if not done and logs[i-ii] not in [-1,logs[i]-ii]:
                print(-1)
                print(logs[i-ii],i)
                done = True
    if done: break
if not done:
    minn = breaks.count(1)
    maxx = len(breaks) - breaks.count(0)
    print(minn,maxx)