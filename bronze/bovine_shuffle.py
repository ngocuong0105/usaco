import sys
sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

n = int(input())

shuffle = list(map(int, input().split()))

ids = list(map(int, input().split()))

past_order = [0] * n

# three shuffles.
for _ in range(3):
    for i in range(n):
        past_order[i] = ids[shuffle[i] - 1]
    ids = past_order.copy()

for i in past_order:
	print(i)