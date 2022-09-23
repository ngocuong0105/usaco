n = int(input())
ncows = []
ecows = []
for i in range(n):
	dir, x, y = input().split()
	if dir == 'N':
		ncows.append((i, int(x), int(y)))
	elif dir == 'E':
		ecows.append((i, int(x), int(y)))
ncows.sort(key = lambda cow: cow[1])
ecows.sort(key = lambda cow: cow[2])
dr = {'N':(0,1),'E':(1,0)}
eat = [float('inf')]*n
for c1 in ncows:
    for c2 in ecows:
        a,b = c1[1],c1[2]
        c,d = c2[1],c2[2]
        if a-c < 0 or d-b < 0 or a-c == d-b: continue
        if a-c > d-b:
            if a-c > eat[c1[0]]:continue
            eat[c2[0]] = min(eat[c2[0]], a-c)
        else:
            if d-b > eat[c2[0]]:continue
            eat[c1[0]] = min(eat[c1[0]], d-b)
for v in eat:
    if v != float('inf'):
        print(v)
    else:
        print('Infinity')
