from collections import Counter
from itertools import accumulate


n = int(input())
nums = list(map(int,input().split()))
nums = [num % n for num in nums]
cum = list(accumulate(nums))
cum = [0]+[num % n for num in cum]
c = Counter(cum)

print(sum((v*(v-1))//2 for v in c.values()))