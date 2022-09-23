import sys
sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

N = int(input())
measurements = []
for _ in range(N):
	time, name, addition = input().split()
	measurements.append([int(time), name, int(addition)])


res = 0
measurements.sort()
display = []
cows = {'Bessie':7,'Mildred':7,'Elsie':7}
for day, name, milk in measurements:
    cows[name] += int(milk)
    change = 0
    for name in cows:
        if cows[name] == max(cows.values()) and name not in display:
            display.append(name)
            change = 1
        if cows[name] != max(cows.values()) and name in display:
            display.remove(name)
            change = 1
    res += change
print(res)
