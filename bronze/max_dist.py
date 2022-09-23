N = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2
res = 0
for i in range(N-1):
    for j in range(i+1,N):
        res = max(res,dist((x[i],y[i]),(x[j],y[j])))
print(res)