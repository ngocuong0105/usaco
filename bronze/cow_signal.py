import sys
sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")
m, n, k =map(int,(input().split(' ')))
lines = []
for _ in range(m):
    lines.append(input())
for line in lines:
    res = []
    for char in line:
        res.append(char*k)
    print(''.join(res)) 