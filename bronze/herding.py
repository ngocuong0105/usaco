import sys
sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

cows = sorted(list(map(int,input().split())))
if cows[0]+1 == cows[1] == cows[2]-1: print(0)
elif cows[0]+2 == cows[1] or cows[1]+2 == cows[2]: print(1)
else: print(2)
print(max(cows[1]-cows[0],cows[2]-cows[1])-1)
