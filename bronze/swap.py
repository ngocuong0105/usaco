import sys
sys.stdin = open("swap.in", "r")
sys.stdout = open("swap.out", "w")

N, K = tuple(map(int,input().split()))
a1, a2 = tuple(map(int,input().split()))
b1, b2 = tuple(map(int,input().split()))

def reverse(arr,i,j):
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1

def nxt(curr):
    reverse(curr,a1-1,a2-1)
    reverse(curr,b1-1,b2-1)

s = [i+1 for i in range(N)]
curr = list(s)
for i in range(1,K):
    nxt(curr)
    if curr == s:
        K %= i
        break
for i in range(K):
    nxt(s)

for num in s:
    print(num)