import sys

# stdin and stdout

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
x5, y5, x6, y6 = map(int, sys.stdin.readline().split())

def contained(a,b):
    return b[0]<= a[0] <= a[1] <= b[1]

def overlap(a,b):
    return min(a[1],b[1]) <= max(a[0],b[0])

if (contained((x1,x2),(x3,x4)) or (contained((x1,x2),(x5,x6))) or (overlap((x3,x4),(x5,x6)) and contained((x1,x2),(min(x3,x5),max(x4,x6))))) and (contained((y1,y2),(y3,y4)) or (contained((y1,y2),(y5,y6))) or (overlap((y3,y4),(y5,y6)) and contained((y1,y2),(min(y3,y5),max(y4,y6))))): print('NO')
print('YES')
