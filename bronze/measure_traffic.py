import sys
sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")

N = int(input())
sensors = []
for _ in range(N):
    arr = input().split()
    sensors.append([arr[0],int(arr[1]),int(arr[2])])

begin, end = [-float('inf'),float('inf')],[-float('inf'),float('inf')]

for t,s,e in sensors:
    if t == 'on':
        end[0] += s
        end[1] += e
    elif t == 'off':
        end[0] -= e
        end[1] -= s
        if end[0] < 0: end[0]=0
    else:
        end[0] = max(end[0],s)
        end[1] = min(end[1],e)
for t,s,e in sensors[::-1]:
    if t == 'on':
        begin[0] -= e
        begin[1] -= s
        if begin[0]<0: begin[0] = 0
    elif t == 'off':
        begin[0] += s
        begin[1] += e
    else:
        begin[0] = max(begin[0],s)
        begin[1] = min(begin[1],e)
print(*begin)
print(*end)