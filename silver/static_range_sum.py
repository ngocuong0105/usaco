from itertools import accumulate


N, Q = tuple(map(int,input().split()))
nums = list(map(int,input().split()))
cum = [0]+list(accumulate(nums))
for _ in range(Q):
    l, r = tuple(map(int,input().split()))
    print(cum[r]-cum[l])