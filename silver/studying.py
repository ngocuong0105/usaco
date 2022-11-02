#https://codeforces.com/gym/102951/problem/B

N, X = tuple(map(int,input().split()))
nums = sorted(list(map(int,input().split())))
res,i = 0,0
while X > 0 and i < len(nums):
    X -= nums[i]
    i += 1
    res += 1
print(res - (X < 0))