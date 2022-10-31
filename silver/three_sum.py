#https://cses.fi/problemset/task/1641/

def solve(nums,t):
    for i in range(len(nums)-2):
        if i and nums[i][0] == nums[i-1][0]: continue
        j,k = i+1,len(nums)-1 
        while j < k:
            if nums[i][0]+nums[j][0]+nums[k][0] == t:
                return f'{nums[i][1]} {nums[j][1]} {nums[k][1]}'
            elif nums[i][0]+nums[j][0]+nums[k][0] > t:
                k -= 1
            else:
                j += 1
    return 'IMPOSSIBLE'
n, t = tuple(map(int,input().split()))
nums = list(map(int,input().split()))
nums = sorted((num,i+1) for i,num in enumerate(nums))
print(solve(nums,t))
