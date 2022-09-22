import sys
sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")

def shifted(arr,i):
    return arr[-i:] + arr[:-i]
def mult(a,b):
    return sum(x*y for x,y in zip(a,b))
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
res = float('inf')
idx = [i for i in range(N)]
for i in range(N):
    arr = shifted(idx,i)
    res = min(res,mult(nums,arr))
print(res)