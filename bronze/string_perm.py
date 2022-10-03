def solve(nums):
    def perm(nums,path):
        if len(path) == n: 
            res.append(list(path))
            return
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]: continue
            perm(nums[:i]+nums[i+1:],path+[nums[i]])
    res,n = [],len(nums)
    nums.sort()
    perm(nums,[])
    return res