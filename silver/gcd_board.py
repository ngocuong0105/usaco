N = int(input())
nums = list(map(int,input().split()))

def gcd(a,b):
    if a < b: a,b = b,a
    while b:
        a,b = b,a%b
    return a
l,r = [nums[0]],[nums[-1]]
for i in range(1,N):
    l.append(gcd(l[-1],nums[i]))
for i in range(N-2,-1,-1):
    r.append(gcd(r[-1],nums[i]))
r.reverse()
res = max(l[-2],r[1])
for i in range(1,N-1):
    res = max(gcd(l[i-1],r[i+1]),res)
print(res)