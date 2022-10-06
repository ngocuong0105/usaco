import sys
sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out", "w")

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
res = 1
for i in range(N):
    level,r,cnt = [nums[i]],1,0
    targets = set(nums)
    visited = set([nums[i]])
    while level:
        newlevel = []
        for num in level:
            cnt += 1
            for t in nums:
                if abs(t-num) <= r and t not in visited:
                    targets.remove(t)
                    newlevel.append(t)
                    visited.add(t)
        level = newlevel
        r += 1
    res = max(res,cnt)
print(res)