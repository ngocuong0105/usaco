import sys
sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")

N = int(input())
points = []
for _ in range(N):
    points.append(tuple(map(int,input().split())))
res = 0

def area(i,j,k):
    x,y,z = (points[i],points[j],points[k])
    return abs(x[0]-z[0])*abs(x[1]-z[1])

def parallel(i,j,k):
    x,y,z = (points[i],points[j],points[k])
    return x[0] == y[0] and y[1] == z[1]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if parallel(i,j,k):
                res = max(res, area(i,j,k))
print(res)