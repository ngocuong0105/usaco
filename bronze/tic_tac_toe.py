import sys
sys.stdin = open("tttt.in", "r")
sys.stdout = open("tttt.out", "w")

mat = []
for _ in range(3):
    mat.append(input())

single,double = set(),set()
for row in mat:
    if len(set(row)) == 1: single.add(row[0])
    if len(set(row)) == 2: double.add(tuple(sorted(list(set(row)))))
for j in range(3):
    col = []
    for i in range(3):
        col.append(mat[i][j])
    if len(set(col)) == 1: single.add(col[0])
    if len(set(col)) == 2: double.add(tuple(sorted(list(set(col)))))

d1 = [mat[0][0],mat[1][1],mat[2][2]]
d2 = [mat[0][2],mat[1][1],mat[2][0]]

if len(set(d1)) == 1: single.add(d1[0])
if len(set(d1)) == 2: double.add(tuple(sorted(list(set(d1)))))
if len(set(d2)) == 1: single.add(d2[0])
if len(set(d2)) == 2: double.add(tuple(sorted(list(set(d2)))))
print(len(single))
print(len(double))