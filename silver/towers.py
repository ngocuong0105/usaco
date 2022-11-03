#https://cses.fi/problemset/task/1073
import bisect
n = int(input())
nums = list(map(int,input().split()))
piles = []
for num in nums:
    i = bisect.bisect_right(piles,num)
    if i == len(piles): piles.append(num)
    piles[i] = num
print(len(piles))