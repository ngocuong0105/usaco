from functools import cache

@cache
def corner(val):
    for i in range (1,val+2):
        if i*i > val: break
        if i*i+1 == val or i*i+i+1 == val:
            return True
    return False

M, N, K = tuple(map(int,input().split()))
spirals = []
for _ in range(K):
    x,y,counter_clock = tuple(map(int,input().split()))
    spirals.append((x-1,y-1,-1,0,1-counter_clock,1))
mat = [[float('inf')]*N for _ in range(M)]
filled = 0
while filled < M*N:
    newspiral = []
    for i,j,di,dj,clockwise,val in spirals:
        if 0 <= i < M and 0 <= j < N:
            filled += mat[i][j] == float('inf')
            mat[i][j] = min(mat[i][j],val)
        if corner(val):
            if clockwise:
                di, dj = dj, -di 
            else:
                di, dj = -dj, di
        i, j = i+di, j+dj
        newspiral.append((i,j,di,dj,clockwise,val+1))
    spirals = newspiral
for row in mat:
    print(' '.join(list(map(str,row))))