def area(t):
    return (t[3]-t[1])*(t[2]-t[0])

def overlap_line(a,b,c,d):
    if not (a<=c<b or c<=a<d): return 0,0
    return max(a,c),min(b,d)

def overlap(a,b):
    x1,x2 = overlap_line(a[0],a[2],b[0],b[2])
    y1,y2 = overlap_line(a[1],a[3],b[1],b[3])
    return (x1,y1,x2,y2)

t1 = tuple(map(int,input().split())) #white
t2 = tuple(map(int,input().split())) #black
t3 = tuple(map(int,input().split())) #black
res = area(t1) - area(overlap(t1,t2)) - area(overlap(t1,t3)) + area(overlap(t1,overlap(t2,t3)))
if res == 0:
    print('NO')
else:
    print('YES')

#%%