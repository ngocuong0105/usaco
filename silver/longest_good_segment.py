# https://www.codechef.com/problems/LGSEG

#%%
def brute_force(nums,N,K,S):
    def can_split(arr):
        curr,seg = arr[0],1
        for num in arr[1:]:
            if curr + num > S:
                seg += 1
                curr = 0
            curr += num
        return seg <= K
    res = -float('inf')
    for i in range(N):
        for j in range(i+1,N+1):
            if can_split(nums[i:j]):
                res = max(res,j-i)
    return res


def solve1(nums,N,K,S):
    def compute(i):
        seg,curr,j = 1,nums[i],i+1
        while seg <= K and j<N:
            if curr + nums[j] > S:
                curr = 0
                seg += 1
            curr += nums[j]
            j += 1
        return j-i-(seg>K)
    return max(compute(i) for i in range(N))

def test(solve,brute_force = brute_force):
    from random import randint
    for _ in range(50):
        nums = [randint(10,100) for _ in range(100)]
        K = randint(1,10)
        S = max(nums)
        if solve(nums,len(nums),K,S) != brute_force(nums,len(nums),K,S):
            print(nums,K,S)
            print('expected: ', brute_force(nums,len(nums),K,S))
            print('actual: ', solve(nums,len(nums),K,S))
            break
    else:
        print("SUCCESS")
# %%
def build(N,start_index):
    up = [[None]*N for _ in range(20)]
    up[0] = start_index
    for i in range(1,20):
        for j in range(N):
            p = up[i-1][j]
            if p == -1:
                up[i][j] = -1
            else:
                up[i][j] = up[i-1][p]
    return up

def call(up, node, K):
    last,jump = node,1
    for i in range(19):
        if node == -1: break
        if K & jump:
            node = up[i][node]
        jump <<= 1
    return last-node

def solve2(nums,N,K,S):
    start_index,j,curr = [],0,0
    for i in range(N):
        curr += nums[i]
        while curr > S:
            curr -= nums[j]
            j += 1
        start_index.append(j-1)
    
    up = build(N,start_index)
    res = 0
    for i in range(N-1,-1,-1):
        res = max(res, call(up,i,K))
    return res
# %%
