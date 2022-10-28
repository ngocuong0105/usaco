#https://codeforces.com/problemset/problem/1478/C

from collections import Counter


def solve_linear(a,b,y):
    return (y-b)/a

def solve(nums,n):
    if any(v != 2 for v in Counter(nums).values()): return 'NO'
    nums.sort(reverse = True)
    b = 0
    for i in range(n):
        x = solve_linear(2*(n-i),b,nums[2*i])
        if int(x) != x or x <= 0:
            return 'NO'
        b += 2*x
    return 'YES'
T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int,input().split()))
    print(solve(nums,n))

