N = int(input())
nums = list(map(int,input().split()))
res = 0
for i in range(N):
    for j in range(i,N):
        res += sum(nums[i:j+1])//(j-i+1) in nums[i:j+1]
print(res)