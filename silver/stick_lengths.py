#https://cses.fi/problemset/task/1074

n = int(input())
nums = sorted(list(map(int,input().split())))
print(sum(abs(num-nums[len(nums)//2]) for num in nums))