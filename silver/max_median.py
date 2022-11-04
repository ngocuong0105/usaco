#https://codeforces.com/contest/1201/problem/C
def cost(nums,x):
    return sum(max(x-num,0) for num in nums)
def solve(inp):
    n, k, nums = inp
    nums.sort()
    nums = nums[n//2:]
    l,r = nums[0]+1,nums[-1]+k+1
    while  l < r:
        m = l+r>>1
        if cost(nums,m)>k:
            r = m
        else:
            l = m+1
    return l-1

n, k = tuple(map(int,input().split()))
nums = list(map(int,input().split()))
inp = (n,k,nums)
print(solve(inp))