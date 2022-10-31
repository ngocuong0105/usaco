#https://codeforces.com/contest/702/problem/C

n, m = tuple(map(int,input().split()))
cities = list(map(int,input().split()))
towers = list(map(int,input().split()))
res = [float('inf')]*len(cities)
j = 0
for i in range(len(cities)):
    while j < len(towers) and towers[j] <= cities[i]:
        res[i] = min(res[i],cities[i]-towers[j])
        j += 1
    res[i] = min(res[i],abs(towers[min(len(towers)-1,j)]-cities[i]))
    if j: j -= 1
print(max(res))

