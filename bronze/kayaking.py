def solve(n, nums):
    nums.sort()
    res = float('inf')
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            arr = nums[:i] + nums[i+1:j] + nums[j+1:]
            res = min(res,sum(abs(y-x) for x,y in zip(arr[::2],arr[1::2])))
    return res
n = int(input())
nums = list(map(int,input().split()))
print(solve(n,nums))
