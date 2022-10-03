import sys
sys.stdin = open("tracing.in", "r")
sys.stdout = open("tracing.out", "w")

N,T = tuple(map(int,input().split()))
cows = [0]+list(map(int,list(input())))
trace = []
for _ in range(T):
    t,x,y = tuple(map(int,input().split()))
    trace.append((t,x,y))
trace.sort()

def simulate(c):
    low,up = float('inf'),-float('inf')
    for K in range(251):
        hooks = [0]*(N+1) # hooks
        infected = [0]*(N+1)
        infected[c] = 1
        for _,x,y in trace:
            hooks[x] += infected[x] 
            hooks[y] += infected[y]
            if not infected[x] and 0 < hooks[y] <= K: 
                infected[x] = 1
            if not infected[y] and 0 < hooks[x] <= K: 
                infected[y] = 1
        if cows == infected:
            low = min(low,K)
            up = max(up,K)
    return [low,up]

cand, low, up = 0,float('inf'),-float('inf')
for c in range(1,N+1):
    if cows[c]: 
        res = simulate(c)
        if res[0] != float('inf'):
            cand += 1
            low = min(res[0],low)
            up = max(res[1],up)

print(cand,low,up if up != 250 else 'Infinity')        