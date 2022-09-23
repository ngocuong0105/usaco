import sys
sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

K, N = map(int,input().split())
mat = []
for _ in range(K):
    mat.append(list(map(int,input().split())))
res = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        flag = (mat[0].index(i) < mat[0].index(j))
        res += all(flag == (mat[k].index(i) < mat[k].index(j)) for k in range(1,K))
print(res)