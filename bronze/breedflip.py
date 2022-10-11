import sys
# sys.stdin = open("breedflip.in", "r")
# sys.stdout = open("breedflip.out", "w")

N = int(input())
a = list(input()) 
b = list(input())

diff = [a[i]!=b[i] for i in range(N)]
compress,i = [],0
while i < len(diff):
    compress.append(diff[i])
    i += 1
    while i < len(diff) and diff[i] == diff[i-1]:
        i += 1
print(compress.count(1))


N,a,b = input(),input(),input()
s = [False]+[x != y for x,y in zip(a,b)] # difference list
print(sum(1 if not x and y else 0 for x,y in zip(s,s[1:])))