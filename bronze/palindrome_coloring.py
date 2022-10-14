from collections import Counter

def solve(k,s):
    c = Counter(s)
    pairs = sum(v//2 for v in c.values())
    pairs_per_string = pairs // k
    add_single = len(s)-pairs_per_string*2*k >= k  
    return pairs_per_string*2 + add_single

T = int(input())
for _ in range(T):
    _,k = tuple(map(int,input().split()))
    s = input()
    print(solve(k,s))
