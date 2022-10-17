from collections import Counter

s = input()
cum_rev,mult = [0],1
for i in range(len(s)-1,-1,-1):
    v = cum_rev[-1] + mult*int(s[i])
    mult = (mult*10) % 2019
    cum_rev.append(v % 2019)
c_rev = Counter(cum_rev)
sm_rev = sum((v*(v-1))//2 for v in c_rev.values())
print(sm_rev)
