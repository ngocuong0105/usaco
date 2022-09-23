import sys
sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")

N, K = map(int,input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
res,i = 0,0
for j in range(len(nums)):
    while nums[j] - nums[i] > K:
        i += 1
    res = max(res, j-i+1)
print(res)