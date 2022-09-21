import sys
sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")

x, y = map(int, input().split())
start = x
res,d,move = 0,1,1
while True:
    if d == 1 and start + d*move >= y > start:  break
    elif d == -1 and start + d*move <= y < start: break
    res += abs(x-(start+d*move))
    x = start+d*move
    d *= -1
    move *= 2
print(res+abs(y-x))