n = int(input())
times = [tuple(map(int,input().split())) for _ in range(n)]
events = [(s,True) for s,_ in times] + [(e,False) for _,e in times]
events.sort()
res,curr = 0,0
for s, is_start in events:
    if is_start:
        curr += 1
    else:
        curr -= 1
    res = max(res,curr)
print(res)
