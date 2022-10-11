import sys
# sys.stdin = open("race.in", "r")
# sys.stdout = open("race.out", "w")

def solve(x):
    speed_up_dist = speed_down_dist = 0
    res, speed = 0,1
    while True:
        speed_up_dist += speed
        res += 1
        if speed_up_dist + speed_down_dist >= K:
            return res
        if speed >= x:
            speed_down_dist += speed
            res += 1
            if speed_up_dist + speed_down_dist >= K:
                return res
        speed += 1

K, N = tuple(map(int,input().split()))
for _ in range(N):
    print(solve(int(input()))) 