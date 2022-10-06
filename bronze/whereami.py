import sys
sys.stdin = open("whereami.in", "r")
sys.stdout = open("whereami.out", "w")

N = int(input())
street = input()

for k in range(1,N+1):
    s = set()
    for i in range(N-k+1):
        if street[i:i+k] in s: break
        s.add(street[i:i+k])
    else:
        print(k)
        break