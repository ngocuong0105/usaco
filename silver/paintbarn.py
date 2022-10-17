from itertools import chain, product
from typing import Any
from utils import submit

def solve(inp) -> Any:
    K, rects = inp
    mat = [[0]*1002 for _ in range(1002)]
    for i,j,x,y in rects:
        mat[i][j] += 1
        mat[x][y] += 1
        mat[x][j] -= 1
        mat[i][y] -= 1 
    # print(mat)
    for i,j in product(range(len(mat)),range(len(mat[0]))):
        n1 = mat[i-1][j] if i else 0
        n2 = mat[i][j-1] if j else 0
        n3 = mat[i-1][j-1] if i and j else 0
        mat[i][j] += n1 + n2 - n3
    # print(mat)
    return sum(v == K for v in chain(*mat))

def read_input() -> tuple:
    N, K  = tuple(map(int,input().split()))
    rects = [tuple(map(int,input().split())) for _ in range(N)]
    return K, rects

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
