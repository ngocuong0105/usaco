from collections import defaultdict
import sys
sys.stdin = open("citystate.in", "r")
sys.stdout = open("citystate.out", "w")
N = int(input())
res,mp = 0,defaultdict(int)
for _ in range(N):
    city, code = input().split()
    mp[city[:2],code] += 1
for i,j in mp.copy():
    res += mp[j,i]*(mp[i,j])*(i!=j)
print(res//2)