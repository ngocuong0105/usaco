# https://cses.fi/problemset/task/1090

n, x = tuple(map(int,input().split()))
nums = sorted(list(map(int,input().split())))
i,j,res = 0,len(nums)-1,0
while i <= j:
    if nums[i]+nums[j] <= x:
        i += 1
    j -= 1
    res += 1
print(res)


