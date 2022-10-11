from collections import defaultdict
import sys
# sys.stdin = open("family.in", "r")
# sys.stdout = open("family.out", "w")

N, a, b = input().split()
N = int(N)
adj = defaultdict(str)
for _ in range(N):
    u,v = input().split()
    adj[v] = u


def lineage(a,adj):
    fam = [a]
    while adj[a]:
        a = adj[a]
        fam.append(a)
    return fam

def solve(a,b,adj):
    fama = lineage(a,adj)
    famb = lineage(b,adj)
    st = set(famb)
    for s in fama:
        if s in st:
            break
    else:
        return 'NOT RELATED'
    fama = fama[:fama.index(s)+1]
    famb = famb[:famb.index(s)+1]
    if len(fama) < len(famb):
        fama,famb = famb,fama
        a,b = b,a
    if len(famb) > 2: return 'COUSINS' 
    elif len(famb) == 1:
        if len(fama) == 2: res = 'mother'
        else:
            res = 'great-'*(len(fama)-3)+'grand-mother'
    elif len(famb) == 2:
        if len(fama) == 2:
            return 'SIBLINGS'
        else:
            res = 'great-'*(len(fama)-3)+'aunt'
    return f'{b} is the {res} of {a}'

print(solve(a,b,adj))

