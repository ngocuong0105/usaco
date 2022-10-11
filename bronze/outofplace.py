import sys
sys.stdin = open("outofplace.in", "r")
sys.stdout = open("outofplace.out", "w")

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
target = sorted(nums)
res = sum(a!=b for a,b in zip(nums,target))
print(res-1)