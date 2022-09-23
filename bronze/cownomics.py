import sys
sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

N, M = map(int,input().split())
spotty,plain = [],[]
for _ in range(N):
    spotty.append(list(input()))
for _ in range(N):
    plain.append(list(input()))
res = 0
spotty = list(zip(*spotty))
plain = list(zip(*plain))
for i in range(M):
    res += (len(set(spotty[i]) & set(plain[i])) == 0)
print(res)