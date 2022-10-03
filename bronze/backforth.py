import sys
sys.stdin = open("backforth.in", "r")
sys.stdout = open("backforth.out", "w")

a = list(map(int,input().split()))
b = list(map(int,input().split()))

res = set()
first, second = 1000,1000

def backtrack(day,first,second,a,b):
    if day == 4:
        res.add(first)
        return
    if day % 2 == 0:
        for i in range(len(a)):
            backtrack(day+1, first - a[i], second + a[i], a[:i] + a[i+1:], b + [a[i]])
    else:
        for i in range(len(b)):
            backtrack(day+1,first + b[i], second - b[i], a + [b[i]], b[:i] + b[i+1:])

backtrack(0,first,second,a,b)
print(len(res))