import sys
sys.stdin = open("sleepy.in", "r")
sys.stdout = open("sleepy.out", "w")

n = int(input())
nums = list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if nums[i-1] > nums[i]: break
print(n-i)