def solve(nums):
    def f(i,val):
        nonlocal res
        res = min(res,abs(sm-2*val))
        if i == len(nums): return
        f(i,val+nums[i])
        f(i,val)
    res,sm = float('inf'),sum(nums)
    f(0,0)

nums = [2,3,4]
def solve(i,v1,v2):
    if i == len(nums):
        return abs(v1-v2)
    return min(solve(i+1,v1+nums[i],v2),solve(i+1,v1,v2+nums[i]))
print(solve(0,0,0))

def solve(nums, allow_empty):
    res = float('inf')
    for mask in range(1-allow_empty, (1 << len(nums)) - (1-allow_empty)):
        s1,s2 = 0,0
        for i in range(len(nums)):
            if mask & (1<<i):
                s1 += nums[i]
            else:
                s2 += nums[i]
        res = min(res,abs(s1-s2))
    return res