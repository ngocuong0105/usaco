N, t = tuple(map(int,input().split()))
nums = list(map(int,input().split()))
d = {}
for i,num in enumerate(nums):
    if t-num in d:
        print(i+1,d[t-num]+1)
        break
    d[num] = i
else:
    print('IMPOSSIBLE')