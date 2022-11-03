#https://codeforces.com/contest/762/problem/B

def solve(inp):
    a,b,c,mouses = inp
    usb = sorted([int(p) for p,t in mouses if t == 'USB'])
    ps = sorted([int(p) for p,t in mouses if t == 'PS/2'])
    cnt, cost, i, j = 0,0,0,0
    while a > 0 and i < len(usb):
        cnt += 1
        cost += usb[i]
        i += 1
        a -= 1
    while b > 0 and j < len(ps):
        cnt += 1
        cost+= ps[j]
        j += 1
        b -= 1
    comb,k = sorted(usb[i:]+ps[j:]),0
    while c > 0 and k < len(comb):
        cnt += 1
        cost += comb[k]
        k += 1
        c -= 1
    return str(cnt) + ' ' + str(cost)

usb, ps, c = tuple(map(int,input().split()))
m = int(input())
mouses = [input().split() for _ in range(m)]
print(solve((usb,ps,c,mouses)))


