import sys
sys.stdin = open("cowtip.in", "r")
sys.stdout = open("cowtip.out", "w")
def tip(row,col):
    for i in range(row+1):
        for j in range(col+1):
            mat[i][j] = 1-mat[i][j]
def furthest(mat):
    row,col = -1,-1
    for i in range(N):
        for j in range(N):
            if mat[i][j]: row,col = i,j
    return row,col

N = int(input())
mat = []
for _ in range(N):
    mat.append(list(map(int,input())))
res = 0
while True:
    i,j = furthest(mat)
    if i == -1: break
    tip(i,j)
    res += 1
print(res)
