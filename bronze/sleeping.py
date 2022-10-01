def poss(nums,t):
    curr = 0
    for i in range(len(nums)):
        curr += nums[i]
        if curr == t: curr = 0
    return curr == 0
def solve(n,nums):
    sm = sum(nums)
    for k in range(n,0,-1):
        if sm % k: continue
        t = sm // k
        if poss(nums,t): return n-k

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int,input().split()))
    print(solve(n,nums))