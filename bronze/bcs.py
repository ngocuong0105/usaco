import sys
sys.stdin = open("bcs.in", "r")
sys.stdout = open("bcs.out", "w")

N, K = map(int,input().split())
orig = []
for _ in range(N):
    orig.append(list(input()))
pieces = []
for _ in range(K):
    p = []
    for _ in range(N):
        p.append(list(input()))
    pieces.append(p)

def translate_match_corner(coord,x,y,f1,f2):
    i = f1(i for i,_ in coord)
    j = f2(jj for ii,jj in coord if ii == i)
    di, dj = i-x, j-y
    for x in range(len(coord)):
        coord[x][0] -= di
        coord[x][1] -= dj
    return set(map(tuple,coord))

def get_coord(p):
    coord = []
    for i in range(len(p)):
        for j in range(len(p[0])):
            if p[i][j] == '#': coord.append([i,j])
    return coord

orig_coord = set(map(tuple,get_coord(orig)))
tx = min(i for i,_ in orig_coord)
ty = min(jj for ii,jj in orig_coord if ii == tx)
bx = max(i for i,_ in orig_coord)
by = max(jj for ii,jj in orig_coord if ii == bx)

for i in range(len(pieces)):
    pieces[i] = get_coord(pieces[i])
done = False
for i in range(len(pieces)):
    for j in range(len(pieces)):
        if i==j or done: continue
        for f1 in [min,max]:
            for f2 in [min,max]:
                c1i = f1(i for i,_ in orig_coord)
                c1j = f2(jj for ii,jj in orig_coord if ii == c1i)
                a = translate_match_corner(pieces[i],c1i,c1j,f1,f2)
                for f1 in [min,max]:
                    for f2 in [min,max]:
                        c1i = f1(i for i,_ in orig_coord)
                        c1j = f2(jj for ii,jj in orig_coord if ii == c1i)
                        b = translate_match_corner(pieces[j],c1i,c1j,f1,f2)
                        if len(a & b) == 0 and (a | b) == orig_coord:
                            if not done: print(min(i+1,j+1),max(i+1,j+1))
                            done = True
                            break