from itertools import accumulate, product
from typing import Any
from utils import submit

def get(mat,i,j):
    if not 0 <= i < len(mat): return 0
    if j >= len(mat[i]): return mat[i][-1]
    elif j < 0: return 0
    return mat[i][j]

def compute(i,j,mat,K):
    val = 0
    for di in range(-K,K+1):
        dj = K - abs(di)
        val += get(mat,i+di,j+dj) - get(mat,i+di,j-dj-1)
    return val

def solve(inp) -> Any:
    N, K, mat = inp
    for i in range(N):
        mat[i] = [0]+list(accumulate(mat[i]))
    res = 0
    for i,j in product(range(N+1),range(N+1)):
        res = max(res,compute(i,j,mat,K))
    return res

def read_input() -> tuple:
    N, K = tuple(map(int,input().split()))
    mat = [list(map(int,input().split())) for _ in range(N)]
    return N, K, mat

submit(solve, read_input, test_cases=[])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
