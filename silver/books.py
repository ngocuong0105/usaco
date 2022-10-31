#https://codeforces.com/contest/279/problem/B

n, t = tuple(map(int,input().split()))
nums = list(map(int,input().split()))
curr,i,res = 0,-1,0
for j in range(len(nums)):
    curr += nums[j]
    while curr > t:
        i += 1
        curr -= nums[i]
    res = max(res,j-i)
print(res)