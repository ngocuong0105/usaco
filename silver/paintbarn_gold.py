from itertools import product
from typing import Any
from utils import submit

L = 10

def get_barn(N,rects):
    mat = [[0]*L for _ in range(L)]
    for idx in range(N):
        i,j,x,y = rects[idx]
        mat[i][j] += 1
        mat[x][y] += 1
        mat[x][j] -= 1
        mat[i][y] -= 1
    return get_cum(mat)

def get_cum(mat):
    import copy
    cum = copy.deepcopy(mat)
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i>0: cum[i][j] += cum[i-1][j]
            if j>0: cum[i][j] += cum[i][j-1]
            if i>0 and j>0: cum[i][j] -= cum[i-1][j-1]
    return cum

def compress_barn(K,mat):
    actual = [[0]*len(mat[0]) for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == K:
                actual[i][j] = -1
            elif mat[i][j] == K-1:
                actual[i][j] = 1
    return actual

def get_rect_area(actual,a,b,x,y):
    # return cum[x][y] - cum[a][y] - cum[x][b] + cum[a][b]
    val = 0
    for i in range(a,x):
        for j in range(b,y):
            val += actual[i][j]
    return val

def max_subarray(actual,i,j):
    curr, res = 0, -float('inf')
    for idx in range(len(actual[0])-1):
        curr += get_rect_area(actual,i,idx,j,idx+1)
        if curr < 0: curr = get_rect_area(actual,i,idx,j,idx+1)
        res = max(curr,res)
    return res

def solve(inp) -> Any:
    N, K, rects = inp
    mat = get_barn(N,rects)
    actual = compress_barn(K,mat) # THIS IS CORRECT
    curr = sum(actual[i][j] == -1 for i,j in product(range(len(mat)),range(len(mat))))
    
    cum = get_cum(actual)
    maxx = 0 
    top,bottom,left,right = [0]*len(mat),[0]*len(mat),[0]*len(mat),[0]*len(mat)
    for i in range(len(mat)):
        for j in range(i,len(mat)):
            maxx = max(maxx, max_subarray(actual,i,j))
            top[j] = max(top[j],maxx)
            bottom[i] = max(bottom[j],maxx)
            for idx in range(len(mat)):
                left[idx] = max(left[idx],maxx)
                right[idx] = max(right[idx],maxx)
            # top_sum,left_sum,right_sum,bottom_sum = 0,0,0,0
            # for idx in range(len(mat)):
            #     top_sum = max(0,top_sum + get_rect_area())
            #     left_sum = max(0,left_sum + get_rect_area())
            #     right_sum = max(0,right_sum + get_rect_area())
            #     bottom_sum = max(0,bottom_sum + get_rect_area())
                # top[idx] = max(top[i],top_sum)
                # left[idx] = max(left[idx],left_sum)
                # right[idx] = max(right[idx],right_sum)
                # bottom[idx] = max(bottom[idx],bottom_sum)
                # maxx = max(maxx,top[i],left[i],right[i],bottom[i])
    # NEXT TASK
    # Check for cases 1 and 2 if top, bottom, left, right are correct
    for i in range(2,len(mat)):
        top[i] = max(top[i],top[i-1])
        left[i] = max(left[i],left[i-1])
        right[i] = max(right[i],right[i-1])
        bottom[i] = max(bottom[i],bottom[i-1])
    for i in range(1,len(mat)):
        # maxx = max(maxx, top[i] + bottom[200-i], left[i] + right[200-i])
        maxx = max(maxx, top[i] + bottom[i], left[i] + right[i])
    return curr + maxx

def read_input() -> tuple:
    N, K = tuple(map(int,input().split()))
    rects = [tuple(map(int,input().split())) for _ in range(N)]
    return N, K, rects

submit(solve, read_input, test_cases=[1,2])
#%%
# from utils import print_mismatch
# print_mismatch(test_cases=[])
