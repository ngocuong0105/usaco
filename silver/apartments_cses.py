#https://cses.fi/problemset/task/1084

n,m,k = tuple(map(int,input().split()))
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
res,i,j = 0,0,0
while i < len(a) and j < len(b):
    if b[j]+k < a[i]:
        j += 1
    elif a[i]+k < b[j]:
        i += 1
    else:
        res += 1
        i += 1
        j += 1
print(res)