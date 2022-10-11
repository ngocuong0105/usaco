import sys
import gc
sys.stdin = open("milkorder.in", "r")
sys.stdout = open("milkorder.out", "w")

N,M,K = tuple(map(int,input().split()))
order = list(map(int,input().split()))
pos = [None]*N
done = False

def compatible(pos,order):
    j = 0
    for i in range(N):
        if j == len(rem): break
        if pos[i] == None:
            pos[i] = rem[j]
            j += 1
    mp = {num:i for i,num in enumerate(pos)}
    for a,b in zip(order,order[1:]):
        if mp[a] > mp[b]: return False
    return True

for _ in range(K):
    cow,i = tuple(map(int,input().split()))
    pos[i-1] = cow
    if cow == 1: 
        res = i-1
        done = True
if not done:
    rem = [cow for cow in order if cow not in set(pos+[1])]
    for idx in range(N):
        if pos[idx] != None: continue
        pos_copy = list(pos)
        pos_copy[idx] = 1
        if compatible(pos_copy,order):
            res = idx
            break
gc.collect()
print(res+1)